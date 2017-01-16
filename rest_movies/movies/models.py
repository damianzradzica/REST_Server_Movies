from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    mail = models.EmailField(max_length=64, blank = True)
    
    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)
    
class Movies(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name = 'movie_director', null = True)
    actors = models.ManyToManyField(Person, through = 'Role', blank = True, related_name = 'movie_actors',  null = True)
    year = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title
    
class Role(models.Model):   #tutaj pytanie, czy intermediate model powinien mieć jeszcze klucz obcy
    movie = models.ForeignKey(Movies, on_delete = models.CASCADE, related_name = 'Movie_movie')
    person = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = 'Person_movie')
    role = models.CharField(max_length=128, null = True)
    
    def __str__(self):
        return self.role

    
    
    