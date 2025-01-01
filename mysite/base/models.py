from django.db import models

from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel, # To add a footer text snippet to your admin interface
)

# import parentalKey:
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

# import AbstractEmailForm and AbstractFormField:
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

from wagtail.snippets.models import register_snippet

# import RichTextField:
from wagtail.fields import RichTextField

# import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin:
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)

@register_setting
class NavigationSettings(BaseGenericSetting):
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    mastodon_url = models.URLField(verbose_name="Mastodon URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
            ],
            "Social settings",
        )
    ]

@register_snippet
class FooterText(
    # DraftStateMixin is an abstract model that you can add to any non-page Django model. You can use it for drafts or unpublished changes. The DraftStateMixin requires RevisionMixin.
    DraftStateMixin,
    #RevisionMixin is an abstract model that you can add to any non-page Django model to save revisions of its instances. Every time you edit a page, Wagtail creates a new Revision and saves it in your database. You can use Revision to find the history of all the changes that you make. Revision also provides a place to keep new changes before they go live.
    RevisionMixin,
    # PreviewableMixin is a Mixin class that you can add to any non-page Django model to preview any changes made.
    PreviewableMixin,
    # TranslatableMixin is an abstract model you can add to any non-page Django model to make it translatable.
    TranslatableMixin,
    models.Model,
):

    # your FormField model inherits from AbstractFormField. 
    # With AbstractFormField, you can define any form field type of your choice in the admin interface. 
    # page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields') defines a parent-child relationship between the FormField and FormPage models.
    class FormField(AbstractFormField):
        page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')

    # your FormPage model inherits from AbstractEmailForm. 
    # Unlike AbstractFormField, AbstractEmailForm offers a form-to-email capability. 
    # Also, it defines the to_address, from_address, and subject fields. It expects a form_fields to be defined.
    class FormPage(AbstractEmailForm):
        intro = RichTextField(blank=True)
        thank_you_text = RichTextField(blank=True)

        content_panels = AbstractEmailForm.content_panels + [
            FormSubmissionsPanel(),
            FieldPanel('intro'),
            InlinePanel('form_fields', label="Form fields"),
            FieldPanel('thank_you_text'),
            MultiFieldPanel([
                FieldRowPanel([
                    FieldPanel('from_address'),
                    FieldPanel('to_address'),
                ]),
                FieldPanel('subject'),
            ], "Email"),
        ]

    body = RichTextField()

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    # The __str__ method defines a human-readable string representation of an instance of the FooterText class. It returns the string “Footer text”.
    def __str__(self):
        return "Footer text"
    # The get_preview_template method determines the template for rendering the preview. It returns the template name “base.html”.
    def get_preview_template(self, request, mode_name):
        return "base.html"
    # The get_preview_context method defines the context data that you can use to render the preview template. It returns a key “footer_text” with the content of the body field as its value.
    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}
    #The Meta class holds metadata about the model. It inherits from the TranslatableMixin.Meta class and sets the verbose_name_plural attribute to “Footer Text”.
    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"