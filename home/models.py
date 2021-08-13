from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    """Homepage Model"""

    templates = "home/home_page.html"
    max_count = 1 # Limits the number of homepages to 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_image")
    ]
    
    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

