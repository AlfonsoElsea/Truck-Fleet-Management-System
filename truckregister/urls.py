from django.urls import path
from . import views

app_name = 'truckregister'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:truck_id>/truck',views.TruckView,name='detail'),
    path('<int:pk>',views.TruckUpdateView.as_view(),name='truck'),
    path('providers', views.ProvidersView, name='providers'),
    path('add_truck', views.addTruckView,name='add_truck'),
    path('update_truck/<int:pk>', views.updateTruckView,name='update_truck'),
    path('delete_truck/<int:pk>', views.deleteTruckView,name='delete_truck'),
    path('edit_odometer/<int:pk>', views.editOdometerView,name='edit_odometer'),
]
