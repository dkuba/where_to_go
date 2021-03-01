from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place', ]


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["sample_image", ]

    def sample_image(self, obj):
        """Изображение"""
        try:
            return format_html('<img src="{}" style="max-height:200px;'
                               'max-width:200px;"/>',
                               obj.image.url)
        except ValueError:
            return format_html('Здесь будет картинка')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
