#encoding:utf-8

from django.db import models

# Create your models here.

"""
NOTE:
====
	there is no need to add an id field to our model 
	because the Django ORM adds it automatically 
	when the syncdb command is executed
"""

class Usuario(models.Model):
	username =  models.CharField(max_length=50L,unique=True)
	email = models.EmailField()
	password = models.CharField(max_length=20L)

	class Meta:
		db_table = 'usuario'

	def __unicode__(self):
		return u'ID: %s | USERNAME: %s | EMAIL: %s' % (self.pk, self.username, self.email)

	def toJson(self,minify=True):
		return {'id': self.pk, 'username': self.username, 'email': self.email}

	def get_username(self):
		return self.username

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

	def set_username(self, username):
		self.username = username

	def set_email(self, email):
		self.email = email

	def set_password(self, password):
		self.password = password


class ManejadorUsuario(object):
	@staticmethod
	def auntenticarUsuario(username, password):
		try:
			return Usuario.objects.filter(username = username, password = password)
		except Exception, e:
			raise e		

	@staticmethod
	def listarUsuarios():
		try:
			return Usuario.objects.all()
		except Exception, e:
			raise e

	@staticmethod
	def editarUsuario(u, e):
		try:			
			user = Usuario.objects.get(username=u)
			if user.get_email() is not e:
				user.set_email(e)
				user.save()
			return True
		except Exception, e:
			return False

	@staticmethod
	def eliminarUsuario(t, l):
		try:
			w = t.split(',')	
			for i in xrange(len(w)):
				if w[i] != l:
					Usuario.objects.filter(username=w[i]).delete()
			return True
		except Exception, e:
			return False




