from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class CommonInfo(models.Model):
    datafile = models.FileField(upload_to="img/%y")
    
    class Meta:
        abstract = True

class Song(CommonInfo):
    ID = models.IntegerField(primary_key = True , unique=True) 
    Name_of_the_song = models.CharField(max_length=100  )
    Duration_in_number_of_seconda = models.PositiveIntegerField() 
    Upload_time = models.DateTimeField(auto_now_add=True , null=True, blank=True, validators=[validate_date])
    
    
    def __unicode__(self):
        return self.Name_of_the_song


    


class Podcast(CommonInfo): 
    peoples = [
        ("people_1", "people_1"),
        ("people_2", "people_2"),
        ("people_3", "people_3"),
        ("people_4", "people_4"),
        ("people_5", "people_5"),
        ("people_6", "people_1"),
        ("people_7", "people_7"),
        ("people_8", "people_8"),
        ("people_9", "people_9"),
        ("people_10", "people_10"),
    
    ]
    ID = models.IntegerField(primary_key = True  , unique=True) 
    Name_of_the_podcast = models.CharField(max_length=100 )
    Duration_in_number_of_seconda = models.PositiveIntegerField() 
    Upload_time = models.DateTimeField(auto_now_add=True , null=True, blank=True,  validators=[validate_date])
    Host = models.CharField(max_length=100)
    Participants = models.CharField(max_length=100, choices = peoples  ,default="people_1")
    file_type = models.CharField(max_length = 10,  default = "podcast", editable = False )
    
    def __unicode__(self):
        return self.Name_of_the_podcast  

    

class Audiobook(CommonInfo):
    ID = models.IntegerField(primary_key = True  , unique=True) 
    Title_of_the_audiobook = models.CharField(max_length=100 )
    Author_of_the_title = models.CharField(max_length=100 )
    Narrator = models.CharField(max_length=100  )
    Duration_in_number_of_seconda = models.PositiveIntegerField()
    Upload_time = models.DateTimeField(auto_now_add=True , null=True, blank=True,  validators=[validate_date])
    file_type = models.CharField(max_length = 10,  default = "audio", editable = False )

    def __unicode__(self):
        return self.Title_of_the_audiobook  

    
    
   