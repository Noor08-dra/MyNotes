from django.contrib import admin
from .models import Notes,Reply,Reactions

# Register your models here.
admin.site.register(Notes)
admin.site.register(Reply)
admin.site.register(Reactions)