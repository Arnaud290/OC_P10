"""Projects views module"""
from rest_framework import generics, permissions
from projects import serializers
from projects.models import Project, Contributor, Issue, Comment
from projects.permissions import (
    IsAuthorProjectOrContributorReadOnly,
    IsAuthorObjectOrContributorReadOnly,
    IsContributorList,
)
from projects.services_views import (
    serializer_method,
    get_contributors_projet,
    create_project,
    create_contributor_projet,
    destroy_object,
    queryset_filter,
    create_issue,
    update_issue,
    create_comment,
)


class ProjectList(generics.ListCreateAPIView):
    """
    View class of the list of projects.
    The user must be authenticated.
    This returns the projects the user is linked to
    """
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return serializer_method(self, 'Project')

    def get_queryset(self):
        return get_contributors_projet(self)

    def perform_create(self, serializer):
        return create_project(self, serializer)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view class of a project,
    the user must be the author of the project
    """
    serializer_class = serializers.ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorProjectOrContributorReadOnly
    ]
    http_method_names = ['get', 'put', 'delete']

    def destroy(self, request, *args, **kwargs):
        return destroy_object(self, 'Project')


class ContributorList(generics.ListCreateAPIView):
    """
    View class of the list of contributors of a project.
    The user must be linked to the project to see the contributors
    or the author of the project to add a contributor
    """
    serializer_class = serializers.ContributorSerializer
    queryset = Contributor.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorProjectOrContributorReadOnly
    ]

    def get_queryset(self, *args, **kwargs):
        return queryset_filter(self, 'project_id')

    def get_serializer_class(self):
        return serializer_method(self, 'Contributor')

    def perform_create(self, serializer):
        return create_contributor_projet(self, serializer=serializer)


class ContributorDelete(generics.DestroyAPIView):
    """
    View class for removing contributors from a project.
    The user must be the author of the project to delete a contributor
    """
    serializer_class = serializers.ContributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorProjectOrContributorReadOnly
    ]

    def get_queryset(self):
        queryset = Contributor.objects.filter(pk=self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        return destroy_object(self, 'Contributor')


class IssueList(generics.ListCreateAPIView):
    """
    View class of the list of issues of a project.
    The user must be a contributor to the project
    """
    queryset = Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsContributorList
    ]

    def get_queryset(self):
        return queryset_filter(self, 'project_id')

    def get_serializer_class(self):
        return serializer_method(self, 'Issue')

    def perform_create(self, serializer):
        return create_issue(self, serializer)


class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Project issue detail view class.
    The user must be the author of the issue
    """
    queryset = Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorObjectOrContributorReadOnly
    ]
    http_method_names = ['put', 'delete']

    def perform_update(self, serializer):
        return update_issue(self, serializer)

    def destroy(self, request, *args, **kwargs):
        return destroy_object(self, 'Issue')


class CommentList(generics.ListCreateAPIView):
    """
    View class of the comments list.
    The user must be a contributor to the project
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsContributorList
    ]

    def get_queryset(self):
        return queryset_filter(self, 'issue_id')

    def get_serializer_class(self):
        return serializer_method(self, 'Comment')

    def perform_create(self, serializer):
        create_comment(self, serializer)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View class detail comments.
    The user must be the author of the comments
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorObjectOrContributorReadOnly
    ]
    http_method_names = ['get', 'put', 'delete']

    def destroy(self, request, *args, **kwargs):
        return destroy_object(self, 'Comment')
