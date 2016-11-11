from django.contrib import admin

from your_snippets.api.models import Snippet, Tag, SavedImage


admin.site.register(Snippet)
admin.site.register(Tag)
admin.site.register(SavedImage)
