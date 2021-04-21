from django.db import models

# Create your models here.

class Research(models.Model):
    id = models.IntegerField(blank=False,unique=True,primary_key=True)
    heading = models.CharField(max_length=64, blank=False)
    imagePath = models.ImageField(upload_to='research_media',blank=True, null=True)
    desc = models.TextField(blank=True)
    linkName = models.CharField(max_length=64, blank=True)
    externalLink = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return (self.heading)

class Member(models.Model):
    research_name = models.ForeignKey(Research, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=False)
    DESIGNATION = (
        ('Advisor','Advisor'),
        ('Member','Member')
    )
    designation = models.CharField(max_length=64, choices=DESIGNATION, default='Member')

    def __str__(self):
        return (self.name)

class Contact(models.Model):
    name = models.CharField(max_length=64, blank=False)
    designation = models.CharField(max_length=64, blank=True)
    department = models.CharField(max_length=128, blank=False)
    college = models.CharField(max_length=128, blank=False)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return (self.name)

class Publication(models.Model):
    year = models.IntegerField(default=2021)
    heading = models.CharField(max_length=512, blank=False)
    linkPath = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return (self.heading)

class People(models.Model):
    name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    imagePath = models.ImageField(upload_to='people_pic', blank=True, null=True)

    def __str__(self):
        return (self.name)

class Faculty(models.Model):
    name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    imagePath = models.ImageField(upload_to='people_pic', blank=True, null=True)

    def __str__(self):
        return (self.name)
