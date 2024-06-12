from django.contrib import admin

# Register your models here.
from .models import Members

#Register your models here
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Members, MemberAdmin)