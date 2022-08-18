from django.db import models

from django_coding_devops.models.project import BaseProject


class DepotVscType(models.TextChoices):
    git = 'git', 'Git'


class BaseDepot(models.Model):
    """
    仓库抽象类。

    用户可使用其自定义，比如增加和内部系统的关联关系。

    字段设计参考：https://help.coding.net/openapi#1865896f07c2c6764e52a9a9d877b23a

    TODO: property属性未处理SVN的情况，不知道返回参数啥样的。
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    # TODO: 抽象类很可能不能关联；要允许用户自定义关联的Project模型。
    project = models.ForeignKey(BaseProject, related_name="depots", on_delete=models.CASCADE, verbose_name='项目')
    vsc_type = models.CharField(max_length=8, choices=DepotVscType.choices)

    class Meta:
        abstract = True
        unique_together = ('project', 'name')

    @property
    def https_url(self):
        return f"https://e.coding.net/codingcorp/{self.project.name}/{self.name}.git"

    @property
    def ssh_url(self):
        return f"https://e.coding.net/codingcorp/{self.project.name}/{self.name}.git"

    @property
    def web_url(self):
        return f"https://codingcorp.coding.net/p/{self.project.name}/d/{self.name}"
