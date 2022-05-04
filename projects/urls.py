from django.urls import path
from .views import (
    ProjectList ,
    ProjectTypeList ,
    ProjectDetailView
)

urlpatterns = [
      path('all' , ProjectList , name='all-projects'),
      path('all/type/<int:pk>' , ProjectTypeList , name='all-projects-types'),
      path('detail/<int:pk>' , ProjectDetailView.as_view() , name='project-detail'),

]
