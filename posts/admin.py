from django.contrib import admin

# Register your models here.
from posts.models import user,about


admin.site.register(user)
admin.site.register(about)
