from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=[('house', 'Будинок'), ('apartment', 'Квартира')])
    images = models.ManyToManyField('AdImage', related_name='ad', blank=False)
    price = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    area = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title
    
class AdImage(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='ad_images')
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return f"Image for {self.advertisement.title}"