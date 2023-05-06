from django.db import models
from django.contrib.auth import get_user_model

# User
User = get_user_model()

# related name / reverse relationship
# user = User.objects.get()
# user.profile => Profile
# OR 
# profile = Profile.objects.filter(user_id=user.id).last()

# foreign key
# profile = Profile.oobjects.get()
# profile.user => User

# on_delete with cascade
# user u1 => profile p1 
# if u1 is deleted => profile p1 ?
# u1 is deleted p1 will be automatically deleted

# Profile
class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "profile"
    
# Post
class Post(models.Model):
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "post"
    
# LikePost
class LikePost(models.Model):
    post = models.ForeignKey(Post, related_name='like_post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='like_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:        
        db_table = "like_post"
    

    