from django.urls import path , include
from . import views


urlpatterns=[
    path('song/', views.Song_Create.as_view(), name='song'),
    path('song/<int:pk>/', views.Song_Put.as_view(), name='song_put'),
    path('podcast/', views.Podcast_Create.as_view(), name='sonng'),
    path('podcast/<int:pk>/', views.Podcast_Put.as_view(), name='song_put'),
    path('audiobook/', views.Audiobook_Create.as_view(), name='sonng'),
    path('audiobook/<int:pk>/', views.Audiobook_Put.as_view(), name='song_put'),
]    

