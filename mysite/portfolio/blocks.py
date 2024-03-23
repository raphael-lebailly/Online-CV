# import CharBlock, ListBlock, PageChooserBlock, PageChooserBlock, RichTextBlock, and StructBlock:
from wagtail.blocks import (
    CharBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StructBlock,
)

# import ImageChooserBlock:
from wagtail.images.blocks import ImageChooserBlock

from base.blocks import BaseStreamBlock

# add CardBlock:
class CardBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"])
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = "form"
        template = "portfolio/blocks/card_block.html"

# add FeaturedPostsBlock:
# FeaturedPostsBlock uses ListBlock. 
# ListBlock is a structural block type that you can use for multiple sub-blocks of the same type.
# You used it with PageChooserBlock to select only the Blog Page type pages. 
# To better understand structural block types, read the Structural block types documentation.
class FeaturedPostsBlock(StructBlock):
    heading = CharBlock()
    text = RichTextBlock(features=["bold", "italic", "link"], required=False)
    posts = ListBlock(PageChooserBlock(page_type="blog.BlogPage"))

    # icon = "form" and icon = "folder-open-inverse" define custom block icons to set your blocks apart in the admin interface.
    # For more information about block icons, read the documentation on block icons.
    class Meta:
        icon = "folder-open-inverse"
        template = "portfolio/blocks/featured_posts_block.html"


class PortfolioStreamBlock(BaseStreamBlock):
    card = CardBlock(group="Sections")
    featured_posts = FeaturedPostsBlock(group="Sections")