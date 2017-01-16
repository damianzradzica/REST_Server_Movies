from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render
from movies.models import Movies, Person
from movies.serializers import MoviesSerializer, PersonSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class MoviesList(APIView):
    def get(self, request, format=None):
        movie = Movies.objects.all()
        serializer = MoviesSerializer(movie, many = True, context={"request": request})
        return Response(serializer.data)

class PersonList(APIView):
    def get(self, request, format=None):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many = True, context={"request": request})
        return Response(serializer.data)

class PersonView(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, context={"request": request})
        return Response(serializer.data)
    
    def delete(self, request, pk, format = None):
        person = self.get_object(pk)
        person.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    
class MovieView(APIView):
    def get_object(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MoviesSerializer(movie, context={"request": request})
        return Response(serializer.data)
    
    def delete(self, request, pk, format = None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MoviesSerializer(movie, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        
        
        