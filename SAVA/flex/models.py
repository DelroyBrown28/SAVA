""""Flexible Page"""

from django.db import models
from wagtail.core.models import Page
from streams import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField


class FlexPage(Page):
    # @remember:
    # This page generates the blocks/streamfields on the your flex_page.html.
    # Copy/Paste this whole class to make other pages flexibe,
    # Change the template.
    template = 'flex/flex_page.html'

    # @remember:
    # This is the content being rendered on the flex_page.html
    content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichTextBlock()),
            ('simple_richtext', blocks.SimpleRichTextBlock()),
            ('service_cards', blocks.CardBlock()),

        ],
        null=True,
        blank=True
    )

    subtitle = models.CharField(max_length=150, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'


class HomeFlexPage(Page):
    template = 'home/home_page.html'

    content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichTextBlock()),
            ('simple_richtext', blocks.SimpleRichTextBlock()),
            ('service_cards', blocks.CardBlock()),

        ],
        null=True,
        blank=True
    )

    subtitle = models.CharField(max_length=150, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Flexed Home Page'
        verbose_name_plural = 'Flexed Home Pages'
