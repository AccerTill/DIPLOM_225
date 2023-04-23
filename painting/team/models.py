from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default = False)
    # если удаляем пользователя
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



    # models.CASCADE    - если пользователь удалится то и удалятся и его задачи.

    # models.PROTECTED     - запрещено удалять пользователя пока есть какие то задачи

    # models.SET_NULL      - задачи остануться в базе, даже при удалении пользователя,
    #                        но значение в поле пользователь измениться на None.

    # models.SET_DEFAULT   - задачи остануться в базе, даже при удалении пользователя,
    #                        но значение в поле пользователь измениться на данное по умолчанию.


# class Shop(models.Model):
#     title = models.CharField(max_length=100)
#     autor = models.TextField(blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     date_completed = models.DateTimeField(null=True, blank=True)
#     important = models.BooleanField(default = False)
#     # если удаляем пользователя
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title


