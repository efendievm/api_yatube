from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register(r'posts/(?P<post_id>[\d+])/comments', CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
