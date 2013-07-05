from django.contrib import admin
from im.models import Stu, Fi

import reversion

class StuAdmin(admin.ModelAdmin):
	list_display = ('name', )

class FiAdmin(reversion.VersionAdmin):
	pass

admin.site.register(Stu, StuAdmin)
admin.site.register(Fi, FiAdmin)

reversion.register(Stu)