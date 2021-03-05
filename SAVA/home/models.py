from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class HomePage(Page):
    template = 'home/home_page.html'
    max_count = 1
    home_page_title = models.CharField(max_length=50, blank=True, null=True)
    home_page_subtitle = RichTextField(features=["bold", "italic"])
    top_home_page_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    home_page_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    home_page_panels = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichTextBlock()),
            ('simple_richtext', blocks.SimpleRichTextBlock()),
            ('service_cards', blocks.CardBlock()),

        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel('home_page_title'),
        FieldPanel('home_page_subtitle'),
        ImageChooserPanel('top_home_page_image'),
        PageChooserPanel('home_page_cta'),
        StreamFieldPanel('home_page_panels'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
