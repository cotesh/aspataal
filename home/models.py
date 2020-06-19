from django.db import models
from django.utils.timezone import now

# Create your models here.
class Doctor(models.Model):
    docNo = models.AutoField(primary_key=True)
    docname = models.CharField(max_length=100)
    busyTill = models.DateTimeField(default=now)
    pats = models.IntegerField(default=0,blank=True)
    capacity = models.CharField(max_length=20, blank = True)

    def __str__(self):
        if self.pats==2:
            return self.docname+f'   {self.pats} '+self.capacity
        else:
            return self.docname+f'   {self.pats}'



class Patient(models.Model):
    patNo = models.AutoField(primary_key=True)
    patname = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank = True)
    appointTime = models.DateTimeField(auto_now_add=False, blank= True)

    def __str__(self):
        return self.patname



# class Gyan(models.Model):
#     sno= models.AutoField(primary_key=True)
#     fenku=models.CharField(max_length=100)
#     topic=models.CharField(max_length=50)
#     slug=models.CharField(max_length=120)
#     fullgyan=models.TextField(max_length=5000)
#     waqt=models.DateTimeField(auto_now_add=True, blank=True)


# sno= models.AutoField(primary_key=True)
#     comment=models.TextField()
#     user= models.ForeignKey(User,on_delete=models.CASCADE)
#     gyan= models.ForeignKey(Gyan,on_delete=models.CASCADE)
#     parent= models.ForeignKey('self',on_delete=models.CASCADE, null=True)
#     samay= models.DateTimeField(default=now)