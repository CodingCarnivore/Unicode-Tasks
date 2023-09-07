from django.db import models
class CaughtPokemon(models.Model):
    name=models.CharField(max_length=100)
    level=models.PositiveIntegerField(default=0)

    sprite=models.ImageField(upload_to='pokemon_sprites/', blank=True, null=True) #even if no img is selected form gets validated due to blank
    #if no image is provided field will store a null value in the database

    height=models.DecimalField(max_digits=5,decimal_places=2,null=True) #max_digits should always be greater than decimal_places
    moves=models.JSONField(null=True) #stores an exact copy of the input text

    def __str__(self): #this method converts object into string and returns a name instead of an object
        return self.name



# Create your models here.
