from django.urls import path
from .views import BoardingHouseListCreate, BoardingHouseRetrieveUpdateDestroy

urlpatterns = [
    path('boardinghouses/', BoardingHouseListCreate.as_view(), name='boardinghouse-list'),
    path('boardinghouses/<int:pk>/', BoardingHouseRetrieveUpdateDestroy.as_view(), name='boardinghouse-detail'),
]
