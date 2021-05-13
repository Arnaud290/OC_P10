from django.http import Http404
from rest_framework import permissions
from .models import Project, Contributor


def get_project(request):
    """Return function of the project according
    to the number "pk" or 'project_id' of the url"""
    try:
        project_id = request.parser_context["kwargs"]["project_id"]
    except KeyError:
        project_id = request.parser_context["kwargs"]["pk"]
    try:
        projet = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404
    return projet


def get_contributors_project(request):
    """Return function of the list of
    contributors of a project"""
    contributors = [
        user.user_id for user in Contributor.objects.filter(
            project_id=get_project(request)
        )
    ]
    if request.user in contributors:
        return True


def permission_method(request, obj=None):
    """Return function of the read or write persmission
    method according to an object or a project number"""
    if request.method in permissions.SAFE_METHODS:
        return get_contributors_project(request)
    if obj:
        return obj.author_user_id == request.user
    return get_project(request).author_user_id == request.user
