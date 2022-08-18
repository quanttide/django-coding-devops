from django.db import models


class BaseProject(models.Model):
    """
    字段参考：https://help.coding.net/openapi#a81b33a2ce9c54e39f7ccc6021d1d2ec
    """
    id = models.IntegerField(primary_key=True, verbose_name='项目ID')
    name = models.IntegerField(unique=True, verbose_name='项目名称')

    class Meta:
        abstract = True
