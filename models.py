from django.db import models


# Create your models here.
class musician(models.Model):
    #   id = models.AutoField(primary_key=True)  by default primary key hisebe nibe django
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      instrument = models.CharField(max_length=100)
      
class album(models.Model):
    # id = models.AutoField(primary_key=True)  by default
    artist = models.ForeignKey(musician,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    release_date =models.DateField()
    num_stars = models.IntegerField()
    
    #tuple create
    rating = (
        (1, "worst"),
        (2,"bad"),
        (3,"not bad"),
        (4,"good"),
    )
    
    #choice
    num_stars = models.IntegerField(choices= rating)
    
    def __str__(self):
         return self.name +", rating: " + str(self.num_stars)
    
def __str__(self):
    return self.first_name + "" + self.last_name



# CREATE TABLE Person (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );

# # class person(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)