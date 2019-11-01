from django.db import models

# Create your models here.
class YoutuberModel(models.Model):
    name = models.CharField(max_length=50)
    profile_img = models.URLField('Profile Image')
    video_url = models.URLField('Video URL')
    description = models.CharField(max_length=500)
    views = models.IntegerField(default=0)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name

class YoutuberCategoryModel(models.Model):
    youtuber_id = models.IntegerField(null=False)
    category_id = models.IntegerField()
    register_date = models.DateTimeField('Register Date')

class SubscriberModel(models.Model):
    user_id = models.IntegerField(null=False)
    youtuber_id = models.IntegerField(null=False)
    register_date = models.DateTimeField('Register Date')

class ReviewModel(models.Model):
    youtuber_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    review_text = models.CharField(max_length=300)
    register_date = models.DateTimeField('Register Date')
    delete_yn = models.CharField(max_length=10)

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)
    register_date = models.DateTimeField('Register Date')

