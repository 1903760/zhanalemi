from django.contrib import admin
from .models import *
from .widgets import *
from django import forms
from django.shortcuts import redirect


# Админка даты альбомов
# class GodAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'date_slug': ('title',)}
#     list_display = ['title']


#  Админка Альбома
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'album_slug': ('title',)}
    list_display = ['title']


class PhotoAdminForm(forms.ModelForm):

    class Meta:
        model = Photo
        widgets = {'image': MultiFileInput}
        exclude = [""]


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm
    list_display = ['image']

    def add_view(self, request, *args, **kwargs):
        images = request.FILES.getlist('image',[])
        is_valid = PhotoAdminForm(request.POST, request.FILES).is_valid()

        if request.method == 'GET' or len(images)<=1 or not is_valid:
            return super(PhotoAdmin, self).add_view(request, *args, **kwargs)
        for image in images:
            album_id=request.POST['album']
            photo = Photo(album_id=album_id, image=image)
            photo.save()
        return redirect('/admin/albome/photo/')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
# admin.site.register(DateAlbums, GodAdmin)