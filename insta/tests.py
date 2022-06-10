from django.test import TestCase
from .models import *

# Create your models here.
class TestTag(TestCase):
  # Set up method
  def setup(self):  
    self.title = Tag(title='title', slug='slug')

  # Testing  instance
  def test_instance(self):
    self.assertTrue(isinstance(self.title,Tag))

  def test_save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    self.title.save(*args, **kwargs)
    tags = Tag.objects.all()
    self.assertTrue(len(tagss) > 0)


class TestPost(TestCase):
  # Set up method
  def setUp(self):
    self.id = Post(id = 'id', name = 'name', content =  'content', caption = 'caption', posted = 'posted', tags = 'tags', user = 'user', likes = 3)

  # Testing  instance
  def test_instance(self):
    self.assertTrue(isinstance(self.id,Post))

  # Testing Save Method
  def test_save_method(self):
    self.id.post_save.connect()
    posts = Post.objects.all()
    self.assertTrue(len(posts) > 0)

  # Testing Delete Method
  def test_delete_method(self):
    self.id.post_delete.connect()
    posts = Post.objects.all()
    self.assertTrue(len(posts) == 0)

  
class TestComment(TestCase):
  def setUp(self):
    self.id = Post(post = 'post',	user = 'user', body = 'body',	date = 'date')

  def test_save_method(self):
    self.id.comment_save.connect()
    comments = Comment.objects.all()
    self.assertTrue(len(comments) > 0)

  def test_delete_method(self):
    self.id.comment_delete.connect()
    comments = Comment.objects.all()
    self.assertTrue(len(comments) == 0)


class TestFollow(TestCase):
  def setUp(self):
    self.follower = Follow(follower =  'follower', following = 'following')

  def test_save_method(self):
    self.id.post_save.connect()
    followers = Follow.objects.all()
    self.assertTrue(len(followers) > 0)

  def test_delete_method(self):
    self.id.post_delete.connect()
    followers = Follow.objects.all()
    self.assertTrue(len(followers) == 0)


class TestProfile(TestCase):
  def setUp(self):
    self.user = Profile(user = 'profile',	created = 'date', picture = 'Picture')

  def test_save_method(self):
    self.user.profile_save.connect()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) > 0)

  def test_search_profile(self):
    profiles = Profile.search_profile('Username')
    self.assertTrue(len(profiles)>0)
    
class TestStream(TestCase):
  def setUp(self):
    self.post = Stream(post='post', user='follower.follower', date='post.posted', following='user')

  def test_save_method(self):
    self.post.stream.save()
    

class TestLikes(TestCase):
  def setUp(self):
    self.post = Like(user = 'user_like', post = 'post_like')

  def test_save_method(self):
    self.post.post_save.connect()
    likes = Like.objects.all()
    self.assertTrue(len(likes) > 0)

  def test_save_method(self):
    self.post.post_delete.connect()
    likes = Like.objects.all()
    self.assertTrue(len(likes) == 0)
