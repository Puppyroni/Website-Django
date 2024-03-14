from django.db import models

# Create your models here.
class Image(models.Model):
    category_list = [
        ('TANK', 'Tank'),
        ('MELEE DPS', 'Melee DPS'),
        ('RANGED DPS', 'Ranged DPS'),
        ('MAGICAL DPS', 'Magical DPS'),
        ('HEALER', 'Healer'),
    ]
    
    name = models.CharField(max_length = 100, null = False, blank = False)
    caption = models.CharField(max_length = 150, null = False, blank = False)
    description = models.TextField(null = False, blank = False)
    img = models.CharField(max_length = 100, null = False, blank = False)
    published = models.BooleanField(default = False)
    category = models.CharField(max_length = 100, default = '', choices = category_list)
    
    def __str__(self):
        return f'Image [name => {self.name}]'