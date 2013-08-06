from django.contrib import admin
from im.models import Stu, Product

import reversion

class StuAdmin(admin.ModelAdmin):
	list_display = ('name', )

class ProductAdmin(reversion.VersionAdmin):
	pass

admin.site.register(Stu, StuAdmin)
admin.site.register(Product, ProductAdmin)

reversion.register(Stu)
