from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment1 = models.FileField(upload_to="images", null=True, blank=True)
    attachment2 = models.FileField(upload_to="images", null=True, blank=True)


    def __str__(self) :
        return self.title
    
    # To do the reverse url so that the newly created post is taken as a string

    """
        The difference between reverse and redirect is that redirect redirects the user to the next url but the reverse 
        redirects it as a string to the same url
    """ 
    def get_absolute_url(self):

        return reverse("post-detail", kwargs={"pk": self.pk})
    