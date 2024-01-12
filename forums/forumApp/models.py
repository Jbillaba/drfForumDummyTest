from django.db import models

# Create your models here.
class Post(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=50, blank=True, default='')
    textarea=models.TextField()
    op=models.ForeignKey('auth.user', related_name='Posts', on_delete=models.CASCADE)

    class meta:
        ordering=['created']