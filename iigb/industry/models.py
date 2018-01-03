from django.db import models
from django.db.models import CASCADE
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.core.blocks import StructBlock, CharBlock, TextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtailmarkdown.blocks import MarkdownBlock
from wagtailmarkdown.fields import MarkdownField
from wagtailmarkdown.edit_handlers import MarkdownPanel


@register_snippet
class StaticContent(models.Model):
    text = MarkdownField()

    panels = [
        MarkdownPanel('text'),
    ]

    def __str__(self):
        return self.text


class FindUsOn(models.Model):
    pass


class HeaderBlock(StructBlock):
    text = CharBlock()
    background_image = ImageChooserBlock(required=True)

    class Meta:
        template = "industry/blocks/heading.html"


class PulloutBlock(StructBlock):
    text = MarkdownBlock()
    stat_header = CharBlock()
    stat_text = CharBlock()

    class Meta:
        template = "industry/blocks/pullout.html"


class IndustrySnippetBlock(SnippetChooserBlock):
    target_model = StaticContent

    class Meta:
        template = "industry/blocks/snippet.html"


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
        ('content', MarkdownBlock()),
        ('common_content', IndustrySnippetBlock(target_model=StaticContent)),
    ])

    report_problem = models.ForeignKey(StaticContent, on_delete=CASCADE, null=True, related_name='report_problem')
    sharing_text = models.ForeignKey(StaticContent, on_delete=CASCADE, null=True, related_name='sharing_text')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        SnippetChooserPanel('report_problem'),
        SnippetChooserPanel('sharing_text'),
    ]
