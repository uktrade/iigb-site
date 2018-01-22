from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.blocks import StructBlock, CharBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmarkdown.blocks import MarkdownBlock
from wagtailmarkdown.fields import MarkdownField


class IndustriesLandingPage(Page):
    subpage_types = ['industry.IndustryPage']

    # page fields
    heading = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
    ]

    def get_context(self, request):
        context = super(IndustriesLandingPage, self).get_context(request)
        context['industry_pages'] = IndustryPage.objects.all()
        return context


class MarkdownSectionBlock(StructBlock):
    class Meta:
        template = 'sections/markdown.html'

    # accordion section
    title = CharBlock(max_length=255)
    content = MarkdownBlock()


class IndustryPage(Page):
    subpage_types = ['industry.IndustryPage']

    # lockup and hero are so they can be easily queried per page
    # related industries are not in the model - they are just child pages

    # used by external pages
    description = models.TextField()  # appears in tile
    featured = models.BooleanField(default=False)  # industry appears in home

    # page fields
    heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # accordion
    subsections = StreamField([
        ('markdown', MarkdownSectionBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        ImageChooserPanel('hero_image'),
        FieldPanel('heading'),
        StreamFieldPanel('subsections')
    ]


class SetupGuideLandingPage(Page):
    subpage_types = ['industry.SetupGuidePage']

    # page fields
    heading = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
    ]


class SetupGuidePage(Page):
    # lockup and hero are so they can be easily queried per page

    description = models.TextField(max_length=255)  # appears in tile

    # page fields
    heading = models.CharField(max_length=255)

    # accordion
    subsections = StreamField([
        ('markdown', MarkdownSectionBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('heading'),
        StreamFieldPanel('subsections')
    ]


# Settings (Global Text for the website)


@register_setting
class StaticText(BaseSetting):
    report_problem = MarkdownField()


@register_setting
class NextSteps(BaseSetting):
    industry = MarkdownField()
    setup_guide = MarkdownField()


@register_setting
class ShareSettings(BaseSetting):
    """
    Sharing bar
    """
    text = models.CharField(max_length=255)
    twitter = models.URLField(
        help_text='Twitter URL')
    facebook = models.URLField(
        help_text='Facebook page URL')
    linkedin = models.URLField(
        help_text='Linkedin URL')
    youtube = models.URLField(
        help_text='YouTube channel or user account URL')


@register_setting
class SocialMediaSettings(BaseSetting):
    """
    Social bar at the bottom of the site
    """
    text = models.CharField(max_length=255)
    twitter = models.URLField(
        help_text='Twitter URL')
    facebook = models.URLField(
        help_text='Facebook page URL')
    linkedin = models.URLField(
        help_text='Linkedin URL')
    youtube = models.URLField(
        help_text='YouTube channel or user account URL')