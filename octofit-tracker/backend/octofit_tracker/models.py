from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user_email} - {self.activity_type} ({self.date})"


class Leaderboard(models.Model):
    user_email = models.EmailField()
    team = models.CharField(max_length=255)
    total_calories = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.user_email} - Rank {self.rank}"


class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)  # Easy, Medium, Hard
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
