"""Serialization module of the projects application"""
from rest_framework import serializers
from projects.models import Project, Issue, Contributor, Comment


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serialization class allowing
    the creation and view of a project
    """
    author_user_id = serializers.ReadOnlyField(source='author_user_id.id')

    class Meta:

        model = Project
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    """
    Serialization class allowing
    the view of the list of projects
    """
    author_user_username = serializers.ReadOnlyField(
        source='author_user_id.username'
    )

    class Meta:

        model = Project
        fields = ['id', 'title', 'author_user_id', 'author_user_username']


class ContributorSerializer(serializers.ModelSerializer):
    """Contributor serialization class"""
    project_id = serializers.ReadOnlyField(source='project_id.id')
    is_default = serializers.ReadOnlyField()

    class Meta:

        model = Contributor
        fields = '__all__'


class ContributorListSerializer(serializers.ModelSerializer):
    """Serialization class of the list of contributors"""
    username = serializers.ReadOnlyField(source='user_id.username')

    class Meta:

        model = Contributor
        fields = ['user_id', 'username', 'role']


class IssueSerializer(serializers.ModelSerializer):
    """Class of serialization of issues"""
    author_user_id = serializers.ReadOnlyField(source='author_user_id.id')
    project_id = serializers.ReadOnlyField(source='project_id.id')

    class Meta:

        model = Issue
        fields = '__all__'


class IssueListSerializer(serializers.ModelSerializer):
    """Serialization class of the list of issues"""
    author_username = serializers.ReadOnlyField(
        source='author_user_id.username'
    )
    assignee_username = serializers.ReadOnlyField(
        source='assignee_user_id.username'
    )

    class Meta:

        model = Issue
        fields = [
            'id',
            'author_username',
            'title',
            'description',
            'tag',
            'priority',
            'status',
            'created_time',
            'assignee_username',
        ]


class CommentSerializer(serializers.ModelSerializer):
    """Comment serialization class"""
    author_user_id = serializers.ReadOnlyField(source='author_user_id.id')
    issue_id = serializers.ReadOnlyField(source='issue_id.id')

    class Meta:

        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    """Serialization class of the list of comments"""
    class Meta:

        model = Comment
        fields = ['id', 'description']
