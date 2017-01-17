from django.contrib import admin

from your_snippets.api.models import Snippet, Tag, SavedImage


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'url', 'tags', 'public')
    list_display_links = ('title')
    search_fields = ('tags')
    list_per_page = 25


admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Tag)
admin.site.register(SavedImage)
