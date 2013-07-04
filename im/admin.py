from django.contrib import admin
from im.models import Stu, Fi

class StuAdmin(admin.ModelAdmin):
	list_display = ('name', )

class FiAdmin(admin.ModelAdmin):
	list_display = ('ff', )

admin.site.register(Stu, StuAdmin)
admin.site.register(Fi, FiAdmin)
