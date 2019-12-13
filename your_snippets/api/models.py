from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Tag(models.Model):
    name = models.CharField(max_length=140, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField()
    title = models.CharField(max_length=140, blank=False)
    url = models.CharField(max_length=255, primary_key=True)
    content = models.TextField(default='', blank=True)
    tags = models.CharField(max_length=140, blank=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class SavedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    snippet = models.ForeignKey(Snippet, related_name='images', on_delete=models.PROTECT)

    def __str__(self):
        return self.snippet.title

    class Meta:
        ordering = ('snippet',)
        verbose_name = 'Saved Image'
        verbose_name_plural = 'Saved Images'

    def image_tag(self):
        return mark_safe('<img src="%s" width="500" />' % (self.image.url))

    image_tag.short_description = 'Image'
