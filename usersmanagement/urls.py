from django.urls import path, include
from usersmanagement import views
urlpatterns= [
    path('profile/', views.ProfileTemplateView.as_view(), name='profile'),
    

]