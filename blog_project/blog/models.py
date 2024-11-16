from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    '''Handle the comment model'''
    content = model.TextField()
    created_at = models.DateTimeField(auto_add_now=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=CASCADE)

    def __str__(self):
        '''returns the string representation of the comment'''
        return f"Comment by {self.author.username} on {self.post.title}"
