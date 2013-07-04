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

class Fi(models.Model):
	ff = models.CharField(max_length=100)
	fi = models.FileField(upload_to='file', null=True, blank=True)

	def delete(self, *args, **kwargs):
		storage, path = self.fi.storage, self.fi.path

		super(Fi, self).delete(*args, **kwargs)
		storage.delete(path)

	def __unicode__(self):
		return self.ff