from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    # add the Home section of HomePage:
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    home_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    home_cta = models.CharField(
        blank=True,
        verbose_name="Home CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    home_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Home CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("home_text"),
                FieldPanel("home_cta"),
                FieldPanel("home_cta_link"),
            ],
            heading="Home section",
        ),
        FieldPanel('body'),
    ]