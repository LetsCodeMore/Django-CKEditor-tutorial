from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class BlogPost(models.Model):
    title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False
    )
    # body = RichTextField()
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


