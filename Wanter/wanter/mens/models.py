from django.db import models

# Create your models here.
# class Mens(modlels.Model):
#     title       = models.Charfield(max_length = 120)
#     slug        = models.SlugField(blank =True,unique =True)
#     description = models.TextField()
#     price       = models.DecimalField(decimal_places =2,max_digits =20,default =10.99)
#     image       = models.ImageField(upload_to = upload_image_path, null = True,blank=True)
#     timestamp   = models.DateTimeField(auto_now_add = True)
#     featured    = models.BooleanField(default = False)
#     active      = models.BooleanField(default = True)
#
#     def get_absolute_url(self):
#         return reverse('mens:detail', kwargs={"slug":self.slug})
#
#     def __str__(self):
#         return self.title
#
#     @property
#     def name(self):
#         return self.title
