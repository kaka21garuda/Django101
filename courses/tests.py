from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from .models import Course
from .models import Step

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(title = "Python regular expression", description = "learn to write regular expression in python")
        now = timezone.now()
        self.assertLess(course.created_at, now)

class CourseViewTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title = "Python testing", description = "Learn to write test in pyton")
        self.course2 = Course.objects.create(title = "New course", description = "This is a new course")
        self.step = Step.objects.create(title = "Introduction to Doctests", description = "Learn to write test in docstrings", course = self.course)

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
