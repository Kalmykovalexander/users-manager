from django.db import models


# General model for all groups
class Groups(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Group name')
    description = models.CharField(max_length=300, verbose_name='Description of group')

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'Groups'

    def __str__(self):
        return self.name


# General model for all users
class Users(models.Model):
    username = models.CharField(max_length=100, unique=True, verbose_name='User nickname')
    group = models.ManyToManyField(Groups, through='UsersGroups')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'Users'

    def __str__(self):
        return self.username


class UsersGroups(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'group']]
        db_table = 'Users group'

    def __str__(self):
        return f'User - {self.user}, Group - {self.group}.'