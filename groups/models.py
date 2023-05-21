from django.db import models
from django.urls import reverse
# slugify for remove any char. is not an alpha pit
from django.utils.text import slugify
# to use the user model in this site use get_user_model
from django.contrib.auth import get_user_model
from  django import template
# Create your models here.
register = template.Library()
User = get_user_model()


class Group(models.Model):
    # unique that mean there is not more than one group with this name
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    # editable mean description_html can't be edite
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE())
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE())

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
