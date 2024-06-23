from django.contrib import admin

# Register your models here.
from .models import bookDemo  # Import your models
class BookDemoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'subject',"message","created_date")
    list_display_links = ('name',)

admin.site.register(bookDemo,BookDemoAdmin)