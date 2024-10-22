from django.db import models

# Create your models here.

class UserProfiles(models.Model):

    CLIENT = 'CLIENT'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = (
        (CLIENT, 'Client'),
        (ADMIN, 'Admin'),
    )

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    name = models.TextField(max_length=255, blank=False)
    username = models.TextField(max_length=255, blank=False)
    role = models.CharField(
        max_length=30, choices=ROLE_CHOICES,verbose_name='Role'
    )
    
class Film(models.Model):
    affiche = models.ImageField(upload_to='affiches/')
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    acteur_principal = models.CharField(max_length=255)
    duree = models.DurationField()

    def get_affiche(self, obj):
        request = self.context.get('request')
        if obj.affiche and hasattr(obj.affiche, 'url'):
            return request.build_absolute_uri(obj.affiche.url)
        return None 

class Salle(models.Model):
    libelle = models.TextField(max_length=255)
    nombre_de_place = models.IntegerField()
      

class Projection(models.Model):
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.DurationField(auto_created=160)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    

class Ticket(models.Model):
    numero = models.IntegerField()
    type = models.TextField(max_length=255)
    prix = models.DecimalField(decimal_places=3, max_digits=6)
    projection = models.ForeignKey(Projection, on_delete=models.CASCADE)
    


    
    


   
    



        
        



    
         