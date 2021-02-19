from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import Place, Image

admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["sample_image", ]

    def sample_image(self, obj):
        """Изображение"""
        return format_html(
            '<img src="{url}" max-width={width} max-height={height} '
            'style="max-height:200px;"/>'.format(
                url=obj.image.url,
                width=obj.image.width,
                height=obj.image.height,
            ))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
