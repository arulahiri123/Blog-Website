from django.urls import path
from blog import views


urlpatterns = [
    path('',views.PostListView.as_view(),name = 'post_list'),
    path('about/',views.AboutView.as_view(),name = 'about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name ='post_detail'),
    path('post/new',views.CreatePost.as_view(),name = 'new_post'),
    path('post/<int:pk>/edit',views.UpdatePost.as_view(),name = 'edit_post'),
    path('post/<int:pk>/remove',views.DeletePost.as_view(),name = 'remove_post'),
    path('drafts/',views.DraftListPost.as_view(),name = 'drafts'),
    path('post/<int:pk>/comment/',views.add_comment_to_post , name ='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve ,name ='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove , name ='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish, name = 'post_publish'),
]
