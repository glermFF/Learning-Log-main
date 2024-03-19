from django.contrib import admin
from .models import Topic, Entry
# adminpass

admin.site.register(Topic)
admin.site.register(Entry)