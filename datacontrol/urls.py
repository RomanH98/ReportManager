from django.urls import path
import views


urlpatterns = [
    path('', views.get_plan_start, name='home_get_plan'),
    path('allstores/', views.all_stores, name='all_stores'),
    path('setplan/', views.set_plan, name='set_plan')
]