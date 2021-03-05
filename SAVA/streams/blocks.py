# @remember:
# Blocks connect to the streams templates
# Each block/class below must be added to flex/models.py
from wagtail.core import blocks
from wagtail.core.blocks import DecimalBlock

from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add Your Title")
    text = blocks.TextBlock(required=True, help_text="Add Additional Text")

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = 'edit'
        label = 'Title & Text'


class CardBlock(blocks.StructBlock):

    service_cards_title = blocks.CharBlock(
        required=True, help_text="Add Your Title")

    service_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True)),
                ('service_type', blocks.CharBlock(required=True, max_length=50)),
                ('service_description', blocks.TextBlock(
                    required=True, max_length=250)),
                ('service_price', blocks.DecimalBlock(required=True, decimal_places=2)),
                ('button_to_internal_page', blocks.PageChooserBlock(
                    required=False, help_text="Button to a page on your site")),
                ('button_to_url', blocks.URLBlock(required=False,
                                                  help_text='Button to any website using the URL link')),
            ]
        )
    )

    class Meta:
        template = 'streams/card_block.html'
        icon = 'image'
        label = 'Service Cards'


class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'doc-full'
        label = 'Full Richtext'


class SimpleRichTextBlock(blocks.RichTextBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):

        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Simple Richtext'
