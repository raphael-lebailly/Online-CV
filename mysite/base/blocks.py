# reusable Wagtail custom blocks for different content types in your general-purpose app. 
# You can use these blocks across your site in any order. 
# Let’s take a closer look at each of these blocks.

from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

# ImageBlock is a block that editors can use to add images to a StreamField section.
# ImageBlock inherits from StructBlock. 
# With StructBlock, you can group several child blocks together under a single parent block. 
# Your ImageBlock has three child blocks. 
# The first child block, Image, uses the ImageChooserBlock field block type. 
# With ImageChooserBlock, editors can select an existing image or upload a new one. 
# Its required argument has a value of true, which means that you must provide an image for the block to work.
# The caption and attribution child blocks use the CharBlock field block type, 
# which provides single-line text inputs for adding captions and attributions to your images. 
# Your caption and attribution child blocks have their required attributes set to false. 
# That means you can leave them empty in your admin interface if you want to.
class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"

# The first child block, heading_text, uses CharBlock for specifying the heading text, and it’s required.
# The second child block, size, uses ChoiceBlock for selecting the heading size.
# It provides options for h2, h3, and h4. 
# Both blank=True and required=False make the heading text optional in your admin interface.
class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"

# Your BaseStreamBlock class inherits from StreamBlock.
# StreamBlock defines a set of child block types that you would like to include in all of the StreamField sections across a project.
# This class gives you a baseline collection of common blocks that you can reuse and customize
# for all the different page types where you use StreamField.
# For example, you will definitely want editors to be able to add images and paragraph text to all their pages,
# but you might want to create a special pull quote block that is only used on blog pages.
class BaseStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(icon="pilcrow")
    image_block = ImageBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )