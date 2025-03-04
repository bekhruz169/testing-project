from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Student, Test, TestResult
from .serializers import StudentSerializer, TestSerializer, TestResultSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

    @action(detail=False, methods=['get'], url_path='student/(?P<student_id>\d+)')
    def get_results_by_student(self, request, student_id):
        """Get all test results for a specific student."""
        results = TestResult.objects.filter(student_id=student_id)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='test/(?P<test_id>\d+)')
    def get_results_by_test(self, request, test_id):
        """Get all test results for a specific test."""
        results = TestResult.objects.filter(test_id=test_id)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)
