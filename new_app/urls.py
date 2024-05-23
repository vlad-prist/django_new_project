from django.urls import path
from new_app.views import index

urlpatterns = [
    path('', index),
]