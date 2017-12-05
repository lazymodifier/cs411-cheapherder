# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CheapHerder', '0023_create_custom_index'),
    ]

    operations = [
	migrations.RunSQL(
	"""CREATE VIEW top_prod AS select count("CheapHerder_group".group_id) as groupcount,"CheapHerder_product".item_code  from "CheapHerder_product" left outer join "CheapHerder_group" on "CheapHerder_product".item_code= "CheapHerder_group".product_id_id Group BY "CheapHerder_product".item_code ORDER BY groupcount DESC limit 5;"""
	)
    ]
