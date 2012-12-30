from django.contrib import admin
from news.article.models import List
from news.article.models import Item

class ListAdmin(admin.ModelAdmin):
  pass

class ItemAdmin(admin.ModelAdmin):
  pass

admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemAdmin)
