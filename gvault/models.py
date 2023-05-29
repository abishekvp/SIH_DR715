from django.db import models
# Create your models here.
class regextend(models.Model):
    acc_type = models.CharField(max_length=10)
    orgname = models.CharField(max_length=50)
    description = models.TextField()
    profile_pic = models.BinaryField()
    username = models.CharField(max_length=50)
class projects(models.Model):
    project_title = models.CharField(max_length=100)
    description = models.TextField()
    paper_details = models.BinaryField()
    keywords = models.JSONField()
    username = models.CharField(max_length=50)
class lst(models.Model):
    name = models.CharField(max_length=100)
    From_Date = models.CharField(max_length=10)
    To_Date = models.CharField(max_length=10)   
    doc_list = models.TextField()
    investment = models.CharField(max_length=10,default = "1,00,000")
    eligibility = models.TextField()
    grant_type = models.CharField(max_length=15,default = "National")

