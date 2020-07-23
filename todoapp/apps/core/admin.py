from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'TodoApp Login'
admin.site.site_title = 'TodoApp Admin Panel'
admin.site.index_title = 'TodoApp Admin Panel - Apps'
