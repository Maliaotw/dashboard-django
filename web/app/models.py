from django.db import models

from django.contrib.auth.models import User

import uuid


# Create your models here.

class Asset(models.Model):
    '''
    資產信息表
    '''

    number = models.UUIDField(verbose_name='資產編號', default=uuid.uuid4)
    category = models.ForeignKey("Category", verbose_name='類型', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', verbose_name='部門', on_delete=models.CASCADE)
    remarks = models.TextField(verbose_name="備註", blank=True)

    class Meta:
        verbose_name_plural = "資產信息表"

    def __str__(self):
        return "%s" % (self.number)


class Category(models.Model):
    '''
    分類
    '''
    name = models.CharField(max_length=255, verbose_name='類型名稱')

    class Meta:
        verbose_name_plural = "類型"

    def __str__(self):
        return "%s" % (self.name)


class Department(models.Model):
    '''
    部門
    '''

    name = models.CharField(max_length=255, verbose_name="部門名稱")

    class Meta:
        verbose_name_plural = "部門"

    def __str__(self):
        return "%s" % (self.name)
