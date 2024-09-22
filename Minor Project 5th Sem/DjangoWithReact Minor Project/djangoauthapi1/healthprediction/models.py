from django.db import models

# Create your models here.


class Symtoms(models.Model):
    symtoms_name = models.CharField(max_length=400,null=False)
    
    def __str__(self) -> str:
        return f'{self.id} --> {self.symtoms_name}'
    
    
    
