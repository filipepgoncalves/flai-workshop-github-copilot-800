from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            team="Test Team"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email="test@example.com",
            activity_type="Running",
            duration=30,
            calories_burned=300,
            date=timezone.now()
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.user_email, "test@example.com")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories_burned, 300)


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email="test@example.com",
            team="Test Team",
            total_calories=1000,
            total_activities=5,
            rank=1
        )

    def test_leaderboard_creation(self):
        self.assertEqual(self.entry.user_email, "test@example.com")
        self.assertEqual(self.entry.team, "Test Team")
        self.assertEqual(self.entry.total_calories, 1000)
        self.assertEqual(self.entry.rank, 1)


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A quick morning run",
            difficulty="Medium",
            duration=30,
            calories_estimate=300
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.difficulty, "Medium")
        self.assertEqual(self.workout.duration, 30)
        self.assertEqual(str(self.workout), "Morning Run")


class UserAPITest(APITestCase):
    def test_create_user(self):
        url = '/api/users/'
        data = {
            'name': 'API Test User',
            'email': 'apitest@example.com',
            'team': 'API Team'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API Test User')


class TeamAPITest(APITestCase):
    def test_create_team(self):
        url = '/api/teams/'
        data = {
            'name': 'API Test Team',
            'description': 'Team created via API'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'API Test Team')


class ActivityAPITest(APITestCase):
    def test_create_activity(self):
        url = '/api/activities/'
        data = {
            'user_email': 'apitest@example.com',
            'activity_type': 'Running',
            'duration': 45,
            'calories_burned': 450,
            'date': timezone.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)


class WorkoutAPITest(APITestCase):
    def test_create_workout(self):
        url = '/api/workouts/'
        data = {
            'name': 'API Workout',
            'description': 'Workout created via API',
            'difficulty': 'Hard',
            'duration': 60,
            'calories_estimate': 600
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(Workout.objects.get().name, 'API Workout')
