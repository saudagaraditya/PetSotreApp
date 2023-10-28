from django.contrib import admin
from .models import pets
from django.utils.html import format_html


class customAdmin(admin.ModelAdmin):
    list_display = ['name','species','gender','price','img_display','description']
    list_filter = ['animal_type','gender']
    search_fields = ['species','age']
    list_per_page = 5
    
    def img_display(self,obj):
        return format_html('<img src={} width="90" height="90"/>',obj.image.url)



# Register your models here.
admin.site.register(pets,customAdmin)