from django.test import TestCase
from posts.models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Пост1", content="PostPostPost", author_id=1)
        Post.objects.create(title="Пост2", content="PostPostPost", author_id=2)
        Post.objects.create(title="Пост3", content="PostPostPost", author_id=3)

    def test_posts_titles(self):
        title1 = Post.objects.get(id=1).title
        title2 = Post.objects.get(id=2).title
        title3 = Post.objects.get(id=3).title
        self.assertEquals(title1, "Пост1")
        self.assertEquals(title2, "Пост2")
        self.assertEquals(title3, "Пост3")