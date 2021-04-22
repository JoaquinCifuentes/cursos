from django.urls import path
from . import views
urlpatterns = [ 

    path('', views.index, name="index"),
    path('confirm/<int:id>/<str:name>', views.confirm),
     path('destroy/<int:id>', views.destroy, name="destroy")]