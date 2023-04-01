from django.db import models
from django.utils.text import slugify
from django import forms
# from django.contrib.gis.db import models
# Create your models here.

JOB_TYPE = {
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
}


def image_upload(instance, filename):
    image_names, extension = filename.split(".")
    return "jobs/%s/%s.%s" % (instance.id, instance.id, extension)


class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # location = models.PointField()
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(
        'Job', related_name='jop_apply', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    website = models.URLField()
    upload_cv = models.FileField(upload_to='Apply/')
    cover_letter = models.TextField(max_length=100)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# class Location(models.Model):
#     name = models.CharField(max_length=255)
#     point = models.PointField()

#     def __str__(self):
#         return self.name
