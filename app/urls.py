from django.urls import path
from .views import list, detail, create, update, delete


urlpatterns = [
    path('', list, name='list'),
    path('<int:id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('<int:id>/edit/', update, name='update'),
    path('<int:id>/delete/', delete, name='delete'),
]
