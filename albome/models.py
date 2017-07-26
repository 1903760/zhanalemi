from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Album(models.Model):
    date = models.DateField('Дата проекта')
    title = models.CharField('название', max_length=150, db_index=True)
    album_slug = models.SlugField(max_length=150, db_index=True)
    image = ThumbnailerImageField('изображение', upload_to="albome/photos", blank=True)

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['title']

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Album)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.image.storage, photo.image.path
    storage.delete(path)


class Photo(models.Model):
    album = models.ForeignKey(Album, verbose_name='альбом', related_name='photos')
    image = models.ImageField('изображение', upload_to="albome/photos")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
        ordering = ['album']
        ordering = ['-album__date']



@receiver(post_delete, sender=Photo)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.image.storage, photo.image.path
    storage.delete(path)

