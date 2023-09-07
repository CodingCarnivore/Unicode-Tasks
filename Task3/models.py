from django.db import models
class CaughtPokemon(models.Model):
    name=models.CharField(max_length=100)
    level=models.PositiveIntegerField(default=0)

    sprite=models.ImageField(upload_to='pokemon_sprites/', blank=True, null=True) 

    height=models.DecimalField(max_digits=5,decimal_places=2,null=True) 
    moves=models.JSONField(null=True) 

    def __str__(self): 
        return self.name



# Create your models here.
