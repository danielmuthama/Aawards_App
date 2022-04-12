from django.db import models
import datetime as dt

# cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# project models
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = CloudinaryField("image")
    url = models.URLField(blank=True)
    location = models.CharField(max_length=100, default="Nairobi")
    # usability_rate = models.IntegerField(default=0, blank=True, null=True)
    # content_rate = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
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
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title


# profile models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField("image")
    bio = models.TextField(max_length=250, blank=True, null=True)
    contact = models.CharField(max_length=250, blank=True, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.user.username


# rating models
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rate = models.IntegerField(default=0, blank=True, null=True)
    usability_rate = models.IntegerField(default=0, blank=True, null=True)
    content_rate = models.IntegerField(default=0, blank=True, null=True)
    avg_rate = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        rating = Rating.objects.filter(id=id).first()
        return rating

    def __str__(self):
        return self.user.username

# # DesignRate models
# class DesignRate(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rate = models.IntegerField(default=0)

#     def save_design_rate(self):
#         self.save()

#     def delete_design_rate(self):
#         self.delete()

#     @classmethod
#     def get_design_rate(cls, id):
#         design_rate = DesignRate.objects.filter(project=id).all()
#         return design_rate

#     # calculate average design rate
#     @classmethod
#     def design_rate_average(cls, id):
#         design_rate = DesignRate.objects.filter(project=id).all()
#         sum = 0
#         for rate in design_rate:
#             sum += rate.rate
#         average = sum / len(design_rate)
#         return average

#     def __str__(self):
#         return self.project.title


# # UsabilityRate models
# class UsabilityRate(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rate = models.IntegerField(default=0)

#     # calculate average usablity rate
#     @classmethod
#     def usability_rate_average(cls, id):
#         usability_rate = UsabilityRate.objects.filter(project=id).all()
#         sum = 0
#         for rate in usability_rate:
#             sum += rate.rate
#         average = sum / len(usability_rate)
#         return average

#     def save_usability_rate(self):
#         self.save()

#     def delete_usability_rate(self):
#         self.delete()

#     @classmethod
#     def get_usability_rate(cls, id):
#         usability_rate = UsabilityRate.objects.filter(project=id).all()
#         return usability_rate

#     def __str__(self):
#         return self.project.title


# # UsabilityRate models
# class ContentRate(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rate = models.IntegerField(default=0)

#     @classmethod
#     def content_rate_average(cls, id):
#         content_rate = ContentRate.objects.filter(project=id).all()
#         sum = 0
#         for rate in content_rate:
#             sum += rate.rate
#         average = sum / len(content_rate)
#         return average

#     def save_content_rate(self):
#         self.save()

#     def delete_content_rate(self):
#         self.delete()

#     @classmethod
#     def get_content_rate(cls, id):
#         content_rate = ContentRate.objects.filter(project=id).all()
#         return content_rate

#     def __str__(self):
#         return self.project.title