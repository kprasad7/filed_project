from django.shortcuts import render , redirect
from app1.models import Song, Podcast , Audiobook
from app1.serializers import Song_serializer,Podcast_serializer,Audiobook_serializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


class Song_Create(mixins.CreateModelMixin,
                  generics.GenericAPIView):

    serializer_class = Song_serializer
    queryset = Song.objects.all()


    def post(self , request,*args,**kwargs):
        return self.create(request , *args,**kwargs) 
        
class Song_Put(mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               generics.GenericAPIView):
    serializer_class = Song_serializer
    queryset = Song.objects.all()

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)    

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    
    
class Podcast_Create(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    serializer_class = Podcast_serializer
    queryset = Podcast.objects.all()
    #def get_queryset(self):
       #if self.kwargs['song']:
            #return Song.objects.filter(file_type='song')
    
    
    def post(self , request,*args,**kwargs):
        return self.create(request , *args,**kwargs) 


class Podcast_Put(mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               generics.GenericAPIView):
    serializer_class = Podcast_serializer
    queryset = Podcast.objects.all()

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)    

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)      

class Audiobook_Create(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    serializer_class = Audiobook_serializer
    queryset = Audiobook.objects.all()
    
    def post(self , request,*args,**kwargs):
        return self.create(request , *args,**kwargs) 


class Audiobook_Put(mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               generics.GenericAPIView):
    serializer_class = Audiobook_serializer
    queryset = Audiobook.objects.all()

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)        

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)    

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  




def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)

