from django.db import models

# Create your models here.
class d_request(models.Model):
    new_title = models.CharField(max_length=255)
    # new_dics= HTMLField()
    new_image = models.FileField(upload_to='news/', max_length=250, null=True, default=None)
