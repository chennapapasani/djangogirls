from django.contrib import admin
from .models import  Post




class PostAdmin(admin.ModelAdmin):
    list_display=( "author", "published_date",'title','text')





admin.site.register(Post,PostAdmin)