from django.urls import path
from . import views

urlpatterns = [
   path('http_response/', views.http_response),
   path('render_response/', views.render_response),
]

