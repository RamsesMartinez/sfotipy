from django.contrib import admin

from actions import export_as_excel

from .models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'title', 'order', 'album', 'player', 'es_codlplay')
    list_filter = ('artist', 'album')
    search_fields = ('title', 'artist__first_name', 'artist__last_name')
    list_editable = ('title', 'album')

    actions = (export_as_excel, )

    def es_codlplay(self, obj):
        return obj.id == 1

    es_codlplay.boolean = True

admin.site.register(Track, TrackAdmin)


