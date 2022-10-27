from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostDelete, PostUpdate, PostSearch


urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('search/', PostSearch.as_view(), name='post_search')
]