from django.db import models
from django.conf import settings

# Create your models here.

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(10)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '%s/%s.%s' % (instance.owner.username, pid, extension)

class Photo(models.Model):
    title = models.CharField(max_length = 200, blank = False, default = '')
    image = models.ImageField(upload_to = user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thumbnail_image = models.ImageField(blank = True)
    comment = models.CharField(max_length = 500)
    pub_date = models.DateTimeField(auto_now_add = True)
