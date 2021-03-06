# Generated by Django 3.1.7 on 2021-03-06 22:28

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210306_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='home_page_panels',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Your Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add Additional Text', required=True))])), ('full_richtext', streams.blocks.RichTextBlock()), ('simple_richtext', streams.blocks.SimpleRichTextBlock()), ('service_cards', wagtail.core.blocks.StructBlock([('service_cards_title', wagtail.core.blocks.CharBlock(help_text='Add Your Title', required=True)), ('service_cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('icon_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('service_type', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('service_description', wagtail.core.blocks.TextBlock(max_length=250, required=True)), ('service_offering_1', wagtail.core.blocks.CharBlock(max_length=121, required=True)), ('service_offering_2', wagtail.core.blocks.CharBlock(max_length=121, required=True)), ('service_offering_3', wagtail.core.blocks.CharBlock(max_length=121, required=True)), ('service_price', wagtail.core.blocks.DecimalBlock(decimal_places=2, required=True)), ('button_to_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='Button to a page on your site', required=False)), ('button_to_url', wagtail.core.blocks.URLBlock(help_text='Button to any website using the URL link', required=False))])))]))], blank=True, null=True),
        ),
    ]
