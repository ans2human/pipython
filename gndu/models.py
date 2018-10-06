from django.db import models
from django.utils import timezone


class Authors(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.IntegerField(verbose_name="mobile No.", blank=True, null=True)
    website = models.URLField()
    objects = models.Manager()


    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    # date = timezone.now()
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField(max_length=500)
    author_post = models.ForeignKey(Authors, on_delete=models.CASCADE)
    objects = models.Manager()
    def __str__(self):
        return self.title
