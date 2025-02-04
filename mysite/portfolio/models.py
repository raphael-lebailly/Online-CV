from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from portfolio.blocks import PortfolioStreamBlock


class PortfolioPage(Page):
    #  specifies that your Portfolio page can only be a child page of Home Page. 
    parent_page_types = ["home.HomePage"]
    # Your body field is a StreamField, which uses the PortfolioStreamBlock custom block that 
    # you imported from your portfolio/blocks.py file.
    body = StreamField(
        PortfolioStreamBlock(),
        # blank=True indicates that you can leave this field empty in your admin interface.
        blank=True,
        use_json_field=True,
        help_text="Use this section to list your projects and skills.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]