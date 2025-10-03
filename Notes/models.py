
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notes(models.Model):
    title=models.CharField(max_length=50,blank=True,null=True)
    note_text=models.TextField(null=False,blank=False,max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note_text[:20]

class Reply(models.Model):
    note=models.ForeignKey(Notes,on_delete=models.CASCADE,null=False,blank=False,related_name="replies")
    reply_text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class Reactions(models.Model):
      note=models.ForeignKey(Notes,on_delete=models.CASCADE,related_name='reactions',null=True,blank=True)
      reply=models.ForeignKey(Reply,on_delete=models.CASCADE,related_name='reactions',null=True,blank=True)    
      type=models.CharField(max_length=2)
