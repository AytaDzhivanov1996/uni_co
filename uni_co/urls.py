from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.buy, name='buy'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
]
