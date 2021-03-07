from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (FieldPanel,
                                         FieldRowPanel,
                                         InlinePanel,
                                         MultiFieldPanel,
                                         PageChooserPanel,
                                         StreamFieldPanel)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from streams import blocks


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):
    template = 'contact/contact_page.html'

    intro = RichTextField(blank=True)
    thank_you_title = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    contact_page_panels = StreamField(
        [
            ('service_cards', blocks.CardBlock()),

        ],
        null=True,
        blank=True
    )
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        MultiFieldPanel([

            FieldPanel('thank_you_title'),
            FieldPanel('thank_you_text'),


        ], heading='Thank You Page Text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),

        ], heading='Email Settings'),
        StreamFieldPanel('contact_page_panels'),
    ]
