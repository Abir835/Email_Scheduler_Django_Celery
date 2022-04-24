from django.db import models


# Create your models here.


class EmailForm(models.Model):
    form_email = models.CharField(max_length=50, null=True, blank=True)
    to_email = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(max_length=499, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.IntegerField(default=0, null=True, blank=True)
    is_delete = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.subject
