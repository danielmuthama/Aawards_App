from django.db import models
# from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=124)
    email = models.CharField(max_length=124, unique=True)
    avatar = CloudinaryField('image', null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    @property
    def url_formatted_name(self):
        return self.full_name.replace(' ', '+') or self.username

    @property
    def user_avatar(self):
        return self.avatar if self.avatar else f'https://ui-avatars.com/api/?name={self.url_formatted_name}&background=49c5b6&color=fff'

    def update_user(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    @classmethod
    def get_all_users(cls):
        return cls.objects.all()


# project models
class Project(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True, unique=True)
    description = models.TextField()
    image = CloudinaryField("image")
    url = models.URLField(blank=True)
    location = models.CharField(max_length=100, default="Nairobi")
    date = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def thumbnail(self):
        return self.image.build_url(height=200, crop="pad", format='webp')

    @property
    def project_image(self):
        return self.image.build_url(format='webp')

    @property
    def avg_rate(self):
        return (float(self.avg_content_rate) + float(self.avg_design_rate) + float(self.avg_usability_rate)) / 3

    @property
    def avg_content_rate(self):
        return "{:.1f}".format(self.ratings.aggregate(models.Avg('content_rate'))['content_rate__avg'] or 0)

    @property
    def avg_usability_rate(self):
        return "{:.1f}".format(self.ratings.aggregate(models.Avg('usability_rate'))['usability_rate__avg'] or 0)

    @property
    def avg_design_rate(self):
        return "{:.1f}".format(self.ratings.aggregate(models.Avg('design_rate'))['design_rate__avg'] or 0)

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_project_by_slug(cls, slug):
        project = cls.objects.get(slug=slug)
        return project

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_all_projects_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

    # update project
    def update_project(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_project(self):
        self.slug = slugify(self.title)
        self.save()

    def delete_project(self):
        self.delete()

    def user_voted(self, user_id):
        return self.ratings.filter(user_id=user_id).count() > 0

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


# rating models
class Rating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ratings")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='ratings')
    design_rate = models.IntegerField(default=0)
    usability_rate = models.IntegerField(default=0)
    content_rate = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def avg_rate(self):
        return "{:.1f}".format((self.design_rate + self.usability_rate + self.content_rate) / 3)

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        rating = cls.objects.filter(id=id).first()
        return rating

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-date']
