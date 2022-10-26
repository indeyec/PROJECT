from django.contrib.auth.models import AbstractUser
from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class AdvUser(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=50)

    class Meta(AbstractUser.Meta):
        pass
