import os
from django.db import models
from django_fields import DefaultStaticImageField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    subpage_types = ['industry.IndustriesLandingPage', 'industry.SetupGuideLandingPage']

    # header and hero are so they can be easily queried per page
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('sub_heading'),
        ImageChooserPanel('hero_image'),
    ]
