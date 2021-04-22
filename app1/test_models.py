from django.test import TestCase
from .models import Song , Podcast , Audiobook
from django.utils import timezone

# models test
class SongTest(TestCase):

    def create_song(self, Name_of_the_song="yoyo", Duration_in_number_of_seconda=29):
        return Song.objects.create(Name_of_the_song=Name_of_the_song, Duration_in_number_of_seconda=Duration_in_number_of_seconda , Upload_time =timezone.now())

    def test_song_creation(self):
        w = self.create_song()
        self.assertTrue(isinstance(w, Song))
        self.assertEqual(w.__unicode__(), w.Name_of_the_song)

class PodcastTest(TestCase):

    def create_podcast(self, Name_of_the_podcast="honey", Duration_in_number_of_seconda=29 , Host='amazon', Participants="people_1"):
        return Podcast.objects.create(Name_of_the_podcast=Name_of_the_podcast, Duration_in_number_of_seconda=Duration_in_number_of_seconda ,Host=Host,Participants=Participants, Upload_time =timezone.now())

    def test_podcast_creation(self):
        w = self.create_podcast()
        self.assertTrue(isinstance(w, Podcast))
        self.assertEqual(w.__unicode__(), w.Name_of_the_podcast)

class AudiobookTest(TestCase):

    def create_audiobook(self, Title_of_the_audiobook="wings of fire", Author_of_the_title='kalam',Duration_in_number_of_seconda=29,Narrator="manu"):
        return Audiobook.objects.create(Title_of_the_audiobook=Title_of_the_audiobook, Author_of_the_title=Author_of_the_title ,Duration_in_number_of_seconda=Duration_in_number_of_seconda, Upload_time =timezone.now())

    def test_audiobook_creation(self):
        w = self.create_audiobook()
        self.assertTrue(isinstance(w, Audiobook))
        self.assertEqual(w.__unicode__(), w.Title_of_the_audiobook)        
