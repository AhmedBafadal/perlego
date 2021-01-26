from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CreateBookViewSet


app_name='perlego'


router = DefaultRouter()
router.register('book',BookViewSet)
# router.register('upload', CreateBookViewSet, basename='uploadbook')

urlpatterns = [
    path('upload', CreateBookViewSet.as_view(), name='upload-view'),
    path('', include(router.urls))
    
]

urlpatterns += router.urls