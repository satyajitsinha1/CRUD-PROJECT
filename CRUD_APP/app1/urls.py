from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:roll>/',views.StudentUpdate,name='update'),
    path('delete/<int:roll>/',views.StudentDelete,name='delete'),
]
