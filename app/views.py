from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
import cloudinary
import cloudinary.uploader
import cloudinary.api

from app.models import Project, Rating, User
from app.forms import ProfileForm, ProjectForm, UpdateProjectForm
from app.serializer import ProjectsSerializer, UserSerializer

# Create your views here.


def index(request):
    projects = Project.get_all_projects()
    project_of_the_day = projects.last
    return render(request, 'index.html', {'projects': projects, 'banner_project': project_of_the_day})


@login_required()
def upload(request):
    if request.method == 'POST' and request.FILES['image']:
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save_project()

            return redirect(request.META.get('HTTP_REFERER'), {'success': 'Project Uploaded Successfully'})

    return redirect(request.META.get('HTTP_REFERER'), {'error': 'There was an error uploading'})


@login_required()
def update_project(request, project_id):
    if request.method == 'POST':
        project = Project.objects.get(id=project_id)
        form = UpdateProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'), {'success': 'Project updated Successfully'})

    return redirect(request.META.get('HTTP_REFERER'), {'error': 'There was an error updating'})


# delete project
@login_required()
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete_project()
    return redirect("/profile", {"success": "Project Deleted Successfully"})


@login_required()
def rate_project(request, id):
    if request.method == "POST":

        project = Project.objects.get(id=id)
        current_user = request.user

        design_rate = request.POST["design"]
        usability_rate = request.POST["usability"]
        content_rate = request.POST["content"]

        Rating.objects.create(
            project=project,
            user=current_user,
            design_rate=design_rate,
            usability_rate=usability_rate,
            content_rate=content_rate,
        )

        return redirect(request.META.get('HTTP_REFERER'), {'success': 'Project rated Successfully'})


@login_required()
def single_project(request, slug):
    project = Project.get_project_by_slug(slug)
    user_voted = project.user_voted(request.user.id)
    return render(request, 'single-project.html', {'project': project, 'user_voted': user_voted})


@login_required()
def profile(request):
    title = f'Profile {request.user.full_name}'
    return render(request, 'profile.html', {'title': title})


@login_required()
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            request.user.full_name = form.data['full_name']
            request.user.bio = form.data['bio']
            request.user.save()
        return redirect(request.META.get('HTTP_REFERER'), {'success': 'Profile updated successfully'})


@login_required()
def update_avatar(request):
    if request.method == 'POST' and request.FILES['avatar']:
        profile_image = cloudinary.uploader.upload(request.FILES['avatar'])
        request.user.avatar = profile_image['url']
        request.user.save()
        return redirect(request.META.get('HTTP_REFERER'), {'success': 'Profile updated successfully'})


def search(request):
    if 'q' in request.GET and request.GET["q"]:
        search_term = request.GET.get("q")
        searched_projects = Project.objects.filter(
            title__icontains=search_term)
        title = f"Search results For: {search_term}"

        return render(request, "search.html", {"title": title, "projects": searched_projects})
    else:
        return render(request, "search.html", {"title": title})


class ProjectsList(APIView):
    def get(self, request):
        projects = Project.get_all_projects()
        serializers = ProjectsSerializer(projects, many=True)

        return Response(serializers.data)


class ProfilesList(APIView):
    def get(self, request):
        users = User.get_all_users()
        serializers = UserSerializer(users, many=True)

        return Response(serializers.data)
