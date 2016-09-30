from rest_framework import serializers
from base.models import Course, Iteration, Assessment, Result

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'description')

class IterationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Iteration
        fields = ('id', 'description', 'course', 'users', 'start_date', 'end_date')

class AssessmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assessment
        fields = ('id', 'title', 'description', 'iteration', 'start_date', 'end_date')

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'user', 'assessment', 'submitted', 'score')
