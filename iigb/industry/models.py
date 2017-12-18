from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.core.blocks import StructBlock, CharBlock, TextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet


@register_snippet
class StaticContent(models.Model):
    text = models.TextField()

    panels = [
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text


class HeaderBlock(StructBlock):
    text = CharBlock()
    background_image = ImageChooserBlock(required=True)

    class Meta:
        template = "industry/blocks/heading.html"


class PulloutBlock(StructBlock):
    text = CharBlock()
    stat = CharBlock()

    class Meta:
        template = "industry/blocks/pullout.html"


class IndustryPage(Page):
    """
    header:
       - lockup text
       - hero image


    intro
       - pullout text
       - pullout star

    content
       made up of sections

    next steps
        this is basically a snippet
        but has formatting
    """
    # header
    # heading lockup
    # hero image

    body = StreamField([
        ('heading', HeaderBlock()),
        ('pullout', PulloutBlock()),
        ('content', TextBlock()),
        ('snippet', SnippetChooserBlock(target_model=StaticContent)),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
