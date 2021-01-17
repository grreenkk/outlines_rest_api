from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


#this is used for mapping urls for APIView
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)# we dont need to specify a base_name like the hello-ViewSet because we already added a queryset object in views
#The only time we add a base_name is if there is no queryset attached to the registered view or we are trying to overide the name of the queryset that is associated to it



urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
