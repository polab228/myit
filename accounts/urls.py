from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('grades/', views.grades_view, name='grades'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('finances/', views.finances_view, name='finances'),
    path('electives/', views.electives_view, name='electives'),
]