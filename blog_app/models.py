from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    blog_content = models.TextField(verbose_name='Blog Content Write Here')
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image', blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return str(self.blog_title)