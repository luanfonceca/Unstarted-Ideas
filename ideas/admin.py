#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Luan Fonseca on 2013-09-06.
Copyright (c) 2013 Unstarted-Ideas. All rights reserved.
"""

from django.contrib import admin
from django.db.models.loading import get_models

for model in get_models():
    try: 
        admin.site.register(model)
    except: 
        pass
