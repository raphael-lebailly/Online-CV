from django import forms
from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager # for Tags
from taggit.models import TaggedItemBase # for Tags
from wagtail.snippets.models import register_snippet # for Authors
import datetime

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogPage(Page):
    date = models.DateField("Post date", default=datetime.date.today)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    # Authors
    authors = ParentalManyToManyField('blog.Author', blank=True)

    # Tags:
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    # Add the main_image method:
    def main_image(self):
        date = models.DateField("Post date", default=datetime.date.today)
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('authors', widget=forms.CheckboxSelectMultiple), # Authors
            FieldPanel('tags'), # Tags
        ], heading="Blog information"),
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),    

        # Images:
        # -------------------------------------------------------------------------------------------------------------------------------------
        # Adding the InlinePanel to BlogPage.content_panels makes the gallery images available on the editing interface for BlogPage.
        # -------------------------------------------------------------------------------------------------------------------------------------
        InlinePanel('gallery_images', label="Gallery images"),
    ]        

# Inheriting from Orderable adds a sort_order field to the model to keep track of the ordering of images in the gallery.
class BlogPageGalleryImage(Orderable):
    # -------------------------------------------------------------------------------------------------------------------------------------
    # The ParentalKey to BlogPage is what attaches the gallery images to a specific page.
    # A ParentalKey works similarly to a ForeignKey, but also defines BlogPageGalleryImage as a “child” of the BlogPage model,
    # so that it’s treated as a fundamental part of the page in operations like submitting for moderation, and tracking revision history.
    # -------------------------------------------------------------------------------------------------------------------------------------
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    # -------------------------------------------------------------------------------------------------------------------------------------
    # image is a ForeignKey to Wagtail’s built-in Image model, which stores the actual images. 
    # This appears in the page editor as a pop-up interface for choosing an existing image or uploading a new one.
    # This way, you allow an image to exist in multiple galleries. This creates a many-to-many relationship between pages and images.
    #                                                           ******
    # Specifying on_delete=models.CASCADE on the foreign key means that deleting the image from the system also deletes the gallery entry.
    # In other situations, it might be appropriate to leave the gallery entry in place.
    # For example, if an “our staff” page includes a list of people with headshots, and you delete one of those photos,
    # but prefer to leave the person in place on the page without a photo. 
    # In this case, you must set the foreign key to blank=True, null=True, on_delete=models.SET_NULL.
    # -------------------------------------------------------------------------------------------------------------------------------------
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('author_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'

class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
