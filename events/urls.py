from . import views
from django.urls import path

urlpatterns = [
    path('delete_comment/<int:comment_id>', views.delete_comment,
         name='delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
    path("", views.EventList.as_view(), name="home"),
    path('<slug:slug>/', views.EventDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]