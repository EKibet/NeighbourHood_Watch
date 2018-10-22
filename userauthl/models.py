from django.db import models
from django.contrib.auth.models import User
from neighbourhood.models import Neighbourhood
# Create your models here.

class Profile(models.Model):
    
    profile_path = models.ImageField(upload_to = 'profile_pics/',default='profile_pics/default.jpg')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    is_police = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    community = models.ForeignKey(Neighbourhood, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def image(self):
        if self.profile_path and hasattr(self.profile_path, 'url'):
            return self.profile_path.url

    @classmethod
    def search_by_username(cls,search_term):
        search_result = cls.objects.filter(user__username__icontains=search_term)
        return search_result

    def save_profile(self):
        self.save()
