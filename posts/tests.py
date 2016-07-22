from django.test import TestCase
from posts.models import Post, Comment
from django.contrib.auth.models import User

class PostTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='user1', password='1234qwer')
        User.objects.create(username='user2', password='1234qwer')
        User.objects.create(username='user3', password='1234qwer')
        Post.objects.create(title="Пост1", content="PostPostPost", author_id=1)
        Post.objects.create(title="Пост2", content="PostPostPost", author_id=2)
        Post.objects.create(title="Пост3", content="PostPostPost", author_id=3)
        Comment.objects.create(text="Not bad", author_id=1, post_id=1)
        Comment.objects.create(text="Bad", author_id=1, post_id=2)
        Comment.objects.create(text="Amazing", author_id=2, post_id=2)
        Comment.objects.create(text="Lol", author_id=2, post_id=3)
        Comment.objects.create(text="Wtf", author_id=3, post_id=3)
        Comment.objects.create(text="Omg", author_id=3, post_id=1)

    def test_users(self):
        user1 = User.objects.get(id=1).username
        user2 = User.objects.get(id=2).username
        user3 = User.objects.get(id=3).username
        self.assertEquals(user1, "user1")
        self.assertEquals(user2, "user2")
        self.assertEquals(user3, "user3")

    def test_posts_titles(self):
        title1 = Post.objects.get(id=1).title
        title2 = Post.objects.get(id=2).title
        title3 = Post.objects.get(id=3).title
        self.assertEquals(title1, "Пост1")
        self.assertEquals(title2, "Пост2")
        self.assertEquals(title3, "Пост3")

    def test_comments(self):
        comment1 = Comment.objects.get(id=1).post_id
        comment2 = Comment.objects.get(id=2).post_id
        comment3 = Comment.objects.get(id=3).post_id
        comment4 = Comment.objects.get(id=4).post_id
        comment5 = Comment.objects.get(id=5).post_id
        comment6 = Comment.objects.get(id=6).post_id
        self.assertEquals(comment1, 1)
        self.assertEquals(comment2, 2)
        self.assertEquals(comment3, 2)
        self.assertEquals(comment4, 3)
        self.assertEquals(comment5, 3)
        self.assertEquals(comment6, 1)