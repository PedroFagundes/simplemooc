# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | models.Q(description__icontains=query)
		)


class Course(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField(u'Descrição', blank=True)
	start_date = models.DateField(u'Data de início', blank=True, null=True)
	image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', blank=True, null=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	objects = CourseManager()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'
		ordering = ['name']