from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, \
    CategoryDetailView, search_view, RatePostView, change_rating

urlpatterns = [
    # path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category-posts'),
    path('search/', search_view, name='search'),
    path('post/<int:post_id>/rate/', views.rate_post, name='rate-post'),
    path('post/<int:post_id>/change-rating/', change_rating, name='change-rating'),

]