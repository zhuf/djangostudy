#-*- coding: utf-8 -*-

from django.db import models

class Stu(models.Model):
	name = models.CharField(max_length=100)
	head = models.ImageField(upload_to='photo', null=True, blank=True)

	def delete(self, *args, **kwargs):
		storage, path = self.head.storage, self.head.path

		super(Stu, self).delete(*args, **kwargs)
		storage.delete(path)

	def __unicode__(self):
		return self.name


class Product(models.Model):
	STATE_CHOICES = (
		('DEV', u'开发测试'),
		('TEST', u'前期测试'),
		('ONLINE', u'已上线'),
		('OFFLINE', u'下线')
		)

	product_name = models.CharField(u'产品名', max_length=255, blank=True)
	product_owner = models.CharField(u'产品负责人', max_length=255, blank=True)
	first_dep = models.CharField(u'一级部门', max_length=255, blank=True)
	sec_dep = models.CharField(u'二级部门', max_length=255, blank=True)
	productURL = models.CharField(u'产品服务URL', max_length=255, blank=True)
	onlinetime = models.DateTimeField(u'上线时间', blank=True)
	state = models.CharField(u'状态', max_length=255, choices=STATE_CHOICES, blank=True)
	#cost = models.CharField(u'成本', max_length=20, blank=True)
	offlinetime = models.DateTimeField(u'下线时间', blank=True)
	description = models.CharField(u'描述', max_length=512, blank=True)

	def __unicode__(self):
		return self.product_name
	
	class Meta:
		verbose_name = u'产品'