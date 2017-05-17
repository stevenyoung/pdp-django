from django.test import TestCase
from django.db.utils import IntegrityError

from places.models import Scene

from places.models import Artist
from places.models import Author
from places.models import Director
from places.models import Editor

from places.models import Artwork
from places.models import Movie
from places.models import Book


class ArtistModelTest(TestCase):

  def test_creating_a_new_artist(self):
    a_ = Artist.objects.create()
    self.assertIsInstance(a_, Artist)


class ArtworkModelTest(TestCase):

  def test_cannot_save_artwork_without_artist(self):
    work_ = Artwork()
    with self.assertRaises(IntegrityError):
      work_.save()

  def test_can_save_artwork_with_new_artist(self):
    artist_ = Artist.objects.create()
    work_ = Artwork.objects.create(artist=artist_)
    self.assertIs(isinstance(work_, Artwork), True)


class SceneModelTest(TestCase):

  def test_saving_and_retrieving_scene_descriptions(self):
    author_ = Author.objects.create(first_name="First", last_name="Last")
    work_ = Artwork.objects.create(title="Artwork Title", artist=author_)
    scene = Scene(artwork=work_)
    scene.description = 'the first list item described'
    scene.longitude = -122.41575
    scene.latitude = 37.749202
    scene.save()
    self.assertEqual(Scene.objects.count(), 1)
    scene.delete()
    self.assertEqual(Scene.objects.count(), 0)

  def test_saving_a_movie_to_a_scene(self):
    a_ = Director.objects.create()
    m_ = Movie.objects.create(artist=a_)

    scene = Scene(artwork=m_)
    scene.description = 'the first list item described'
    scene.notes = 'noted'
    scene.name = 'scene name'
    scene.longitude = -122.41575
    scene.latitude = 37.749202

    scene.save()
    self.assertEqual(Scene.objects.count(), 1)
    scene.delete()
    scene.full_clean()
    self.assertEqual(Scene.objects.count(), 0)

  def test_to_dict_instance_method(self):
    author_ = Author.objects.create(first_name="First", last_name="Last")
    work_ = Artwork.objects.create(title="Artwork Title", artist=author_)
    scene = Scene(artwork=work_)
    scene.description = 'the first list item described'
    scene.notes = 'noted'
    scene.name = 'Scene Name'
    scene.longitude = -122.41575
    scene.latitude = 37.749202
    scene.save()
    self.assertIn('latitude', scene.to_dict())
    self.assertIn('artwork', scene.to_dict())
    self.assertIn('artist', scene.to_dict())
    self.assertEqual(Scene.objects.count(), 1)
    scene.delete()
    scene.full_clean()
    self.assertEqual(Scene.objects.count(), 0)

  def test_scene_supports_spatial_fields(self):
    self.fail('finish it!')


class AuthorModelTest(TestCase):

  def test_saving_and_retrieving_authors(self):
    author = Author.objects.create(first_name="First", last_name="Last")
    author.save()


class BookModelTest(TestCase):

  def test_saving_and_retrieving_book(self):
    author_ = Author.objects.create()
    book = Book.objects.create(title="Artwork Title", artist=author_)
    # book.save()
    self.assertIn("Title", book.title)

  def test_can_save_same_author_to_different_books(self):
    author_ = Author.objects.create()
    book1 = Book.objects.create(title="Book 1 Title", artist=author_)
    # book1.save()
    book2 = Book.objects.create(title="Book 2 Title", artist=author_)
    # book2.save()
    self.assertEqual(book1.artist, book2.artist)

  def test_book_can_have_multiple_authors(self):
    _auth1 = Author.objects.create()
    _auth2 = Author.objects.create()
    book_ = Book.objects.create(artist=_auth1)
    book_.author = [_auth1, _auth2]
    book_.save()


class MovieModelTest(TestCase):

  def test_saving_and_retrieving_movies(self):
    dir1_ = Director.objects.create()
    dir2_ = Director.objects.create()
    editor_ = Editor.objects.create()
    movie = Movie.objects.create(title="Movie Title", artist=dir1_)
    movie.director = [dir1_, dir2_]
    movie.editor = [editor_]
    movie.save()
