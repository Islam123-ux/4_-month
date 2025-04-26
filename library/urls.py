from django.urls import path
from . import views

urlpatterns = [
   path('http_response/', views.http_response),
   path('render_response/', views.render_response),
   path('post_list/', views.post_list_view),
   path('post_list/<int:id>/', views.post_detail_view),
   path('post_create/', views.create_post_view),
]

