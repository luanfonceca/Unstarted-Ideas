#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Luan Fonseca on 2013-09-06.
Copyright (c) 2013 Unstarted-Ideas. All rights reserved.
"""

def _(x): return x
from django.db.models import *
from django.contrib.auth.models import User

from django_extensions.db.models import (AutoSlugField,
                                         CreationDateTimeField, 
                                         ModificationDateTimeField)

class Category(Model):
    name = CharField(max_length=100, verbose_name=_('Name'))
    slug = AutoSlugField(populate_from='name', max_length=200)

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return u"%s" % self.name

    # @permalink
    # def get_absolute_url(self):
    #     return 'category_detail', (), {'category_slug': self.slug}

    # @permalink
    # def get_json_url(self):
    #     return 'category-detail', (), {'pk': self.pk}

    # @permalink
    # def get_edit_url(self):
    #     return 'edit_category', (), {'category_id': self.pk}

    # @permalink
    # def get_delete_url(self):
    #     return 'delete_category', (), {'category_id': self.pk}


class Idea(Model):
    name = CharField(max_length=100, verbose_name=_('Name'))
    slug = AutoSlugField(populate_from='name', verbose_name=_('Slug'))
    created_at = CreationDateTimeField(verbose_name=_('Date Created'))
    modified_at = ModificationDateTimeField(
        verbose_name=_('Date Modified'))
    description = TextField(max_length=300, 
        verbose_name=_('Description'))
    is_public = BooleanField(default=False, 
        verbose_name=_('Is Public'))
    is_published = BooleanField(default=False, 
        verbose_name=_('Pusblish Now'))
    views = PositiveIntegerField(default=0, 
        verbose_name=_('Amount of Views'))

    # relations
    # license = ForeignKey(to=License, related_name='ideas', verbose_name=_('Licenses'))
    # patent = ForeignKey(to=Patent, related_name='ideas', verbose_name=_('Patents'))
    user = ForeignKey(to=User, related_name='ideas', 
        verbose_name=_('Author'))
    categories = ManyToManyField(to=Category, related_name='ideas', 
        verbose_name=_('Category'))

    class Meta:
        db_table = 'idea'
        verbose_name = _('Idea')
        verbose_name_plural = _('Ideas')

    def __unicode__(self):
        return u"%s" % self.name

    # @permalink
    # def get_absolute_url(self):
    #     return 'idea_detail', (), {'idea_slug': self.slug}

    # @permalink
    # def get_json_url(self):
    #     return 'idea-detail', (), {'pk': self.pk}

    # @permalink
    # def get_edit_url(self):
    #     return 'edit_idea', (), {'idea_id': self.pk}

    # @permalink
    # def get_delete_url(self):
    #     return 'delete_idea', (), {'idea_id': self.pk}
