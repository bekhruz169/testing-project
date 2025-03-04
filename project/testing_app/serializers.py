from rest_framework import serializers
from .models import Student, Test, TestResult

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'

    def validate_score(self, value):
        """Ensure score does not exceed max_score of the test."""
        test = self.instance.test if self.instance else self.initial_data.get('test')

        if isinstance(test, int):  # If test ID is provided
            test = Test.objects.get(id=test)  # Fetch test instance

        if value > test.max_score:
            raise serializers.ValidationError(f"Score cannot be greater than {test.max_score}.")

        return value
