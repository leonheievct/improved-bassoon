from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,TagViewSet,PostViewSet,CommentViewSet


router = DefaultRouter()
router.register('caregories',CategoryViewSet)
router.register('tags',TagViewSet)
# router.register('post_create',PostCreateViewSet)
router.register('post',PostViewSet)
router.register('comment',CommentViewSet)

urlpatterns = [
    path("",include(router.urls))
]
