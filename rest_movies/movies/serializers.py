from rest_framework import serializers
from movies.models import Movies, Person



class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
#         fields = ('title', 'year', 'description')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
#         fields = ('first_name', 'last_name', 'mail')
    