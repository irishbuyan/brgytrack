from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Resident
    path('residents/', views.resident_list, name='resident_list'),
    path('residents/add/', views.add_resident, name='add_resident'),

    # Blotter
    path('blotter/', views.blotter_list, name='blotter_list'),
    path('blotter/add/', views.add_blotter, name='add_blotter'),

    # Certificate
    path('certificate/', views.issue_certificate, name='certificate'),

    # Reports
    path('reports/', views.reports, name='reports'),

    # Settings
    path('settings/', views.settings, name='settings'),
]