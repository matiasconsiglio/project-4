from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model used to define Event attributes both in back and front end.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        Class for ordering events
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns event title

        Parameters:
        self
        """
        return self.title

    def number_of_likes(self):
        """
        Returns cuantity of likes per event

        Parameters:
        self
        """
        return self.likes.count()
   
    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    """
    Model used to define comments attributes per event both in back
    and front end.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Class for ordering events
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns comment author and content

        Parameters:
        self
        """
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """
        Returns comments edition to post_deail
        
        Parameters:
        self
        """
        return reverse('post_detail', args=[self.post.slug])
