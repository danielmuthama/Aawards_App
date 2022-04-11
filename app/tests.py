from django.test import TestCase
from app.models import User, Project, Rating

# Create your tests here.


class ProjectTestClass(TestCase):  # Project class test
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="john", full_name="john doe"
        )

        self.project = Project(
            title="Test Project",
            description="Test Description",
            image="image.jpg",
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        project = Project.objects.get(id=self.project.id)
        self.assertIsNotNone(project)

    def test_update_method(self):
        self.project.title = 'new title'
        self.project.save_project()
        project = Project.objects.get(id=self.project.id)
        self.assertEqual(self.project.title, project.title)

    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        project = Project.objects.filter(id=self.project.id).exists()
        self.assertFalse(project)


class RatingTestClass(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="john", full_name="john doe"
        )

        self.project = Project(
            title="Test Project",
            description="Test Description",
            image="image.jpg",
            user=user,
        )

        self.rating = Rating(user=user, project=self.project,
                             design_rate=9, usability_rate=8, content_rate=7)

        self.project.save_project()
        self.rating.save_rating()

    def test_save_rating(self):
        rating = Rating.filter_by_id(self.rating.id)
        self.assertIsNotNone(rating)

    def test_delete_rating(self):
        self.rating.delete_rating()
        rating = Rating.objects.filter(id=self.rating.id).exists()
        self.assertFalse(rating)
