"""Services module for views"""
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from projects.models import Project, Contributor, Issue
from projects import serializers


def users_list_id(self):
    """Returns the ID number of contributors to a project"""
    return [
        user.user_id.id for user in Contributor.objects.filter(
            project_id=self.kwargs['project_id']
        )
    ]


def serializer_method(self, model):
    """
    Returns the serialization method
    to use (list or detail)
    """
    get_serializer = 'serializers.' + model + 'ListSerializer'
    post_serializer = 'serializers.' + model + 'Serializer'
    if self.request.method == 'GET':
        return eval(get_serializer)
    return eval(post_serializer)


def queryset_filter(self, obj):
    """Returns the filter to use for the queryset"""
    if obj == 'project_id':
        return self.queryset.filter(project_id=self.kwargs.get(obj))
    if obj == 'issue_id':
        return self.queryset.filter(issue_id=self.kwargs.get(obj))


def create_project(self, serializer):
    """
    Method for creating a project and automatic
    creation of the author contributor
    """
    project = serializer.save(author_user_id=self.request.user)
    contributor = Contributor.objects.create(
        user_id=self.request.user,
        project_id=project,
        role="Author"
    )
    contributor.save()


def get_contributors_projet(self):
    """
    Returns the list of projects to
    which a contributor is linked
    """
    contributors_list = [
        project.project_id for project in Contributor.objects.filter(
            user_id=self.request.user
        )
    ]
    return contributors_list


def create_contributor_projet(self, serializer):
    """How to create a contributor"""
    project_id = Project.objects.get(pk=self.kwargs['project_id'])
    if int(self.request.data['user_id']) in users_list_id(self):
        raise ValidationError(
            "l'utilisateur fait deja partie du projet"
        )
    return serializer.save(project_id=project_id)


def destroy_object(self, obj):
    """Method of deleting an object"""
    if obj == 'Contributor':
        try:
            instance = Contributor.objects.get(
                user_id=User.objects.get(pk=self.kwargs['pk']),
                project_id=Project.objects.get(pk=self.kwargs['project_id'])
            )
            user = User.objects.get(pk=self.kwargs['pk'])
            author_project = Project.objects.get(
                pk=self.kwargs['project_id']
            ).author_user_id
            if user == author_project:
                raise ValidationError(
                    "L'auteur du projet ne peut pas être supprimé"
                )
            self.perform_destroy(instance)
            return Response("Utilisateur supprimé")
        except User.DoesNotExist:
            raise ValidationError("l'utilisateur n'existe pas")
        except Contributor.DoesNotExist:
            raise ValidationError(
                "l'utilisateur n'est pas contributeur du projet"
            )
    instance = self.get_object()
    self.perform_destroy(instance)
    return Response("{} supprimé".format(obj))


def test_user_assignee(self):
    """Method for verifying the membership of a user in a project"""
    if int(self.request.data['assignee_user_id']) not in users_list_id(self):
        raise ValidationError(
            "l'utilisateur assigné n'est pas collaborateur du projet"
        )


def create_issue(self, serializer):
    """How to create an issue"""
    test_user_assignee(self)
    project = Project.objects.get(pk=self.kwargs['project_id'])
    serializer.save(
        author_user_id=self.request.user,
        project_id=project
    )


def update_issue(self, serializer):
    """Method for updating an issue"""
    test_user_assignee(self)
    serializer.save()


def create_comment(self, serializer):
    """Method for creating a comment"""
    issue = Issue.objects.get(pk=self.kwargs['issue_id'])
    serializer.save(
        author_user_id=self.request.user,
        issue_id=issue
    )
