from django.urls import include, path
from rest_framework import routers
from notes import views

router = routers.DefaultRouter()

router.register('notes', views.NotesViews)

urlpatterns = [

    path('', include(router.urls)),
]