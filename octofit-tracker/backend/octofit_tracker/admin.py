from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'team', 'created_at']
    search_fields = ['name', 'email', 'team']
    list_filter = ['team', 'created_at']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'activity_type', 'duration', 'calories_burned', 'date', 'created_at']
    search_fields = ['user_email', 'activity_type']
    list_filter = ['activity_type', 'date', 'created_at']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'team', 'total_calories', 'total_activities', 'rank', 'updated_at']
    search_fields = ['user_email', 'team']
    list_filter = ['team', 'rank', 'updated_at']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'duration', 'calories_estimate', 'created_at']
    search_fields = ['name', 'description', 'difficulty']
    list_filter = ['difficulty', 'created_at']
    ordering = ['-created_at']
