from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from .api_views import QuestionBatchAPIView, TEST_MODE_QUESTIONS
from .models import Question


class QuestionBatchAPIViewTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="tester", password="password")
        self.view = QuestionBatchAPIView.as_view()

    def get_questions(self, query_string):
        request = self.factory.get(f"/api/v1/questions/{query_string}")
        force_authenticate(request, user=self.user)
        response = self.view(request)
        return response

    def test_test_mode_returns_same_questions_every_time(self):
        Question.objects.create(
            question="Random DB question",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_index=0,
            subject="machine_learning",
            difficulty="hard",
        )

        first_response = self.get_questions("?subject=machine_learning&test=true")
        second_response = self.get_questions("?subject=machine_learning&test=true")

        expected_ids = [question["id"] for question in TEST_MODE_QUESTIONS]
        self.assertEqual(first_response.status_code, 200)
        self.assertEqual(second_response.status_code, 200)
        self.assertTrue(first_response.data["test_mode"])
        self.assertEqual(
            [question["id"] for question in first_response.data["questions"]],
            expected_ids,
        )
        self.assertEqual(first_response.data["questions"], second_response.data["questions"])
        self.assertEqual(
            first_response.data["questions"][0]["question"],
            "TEST MODE: Which data structure uses FIFO order?",
        )
