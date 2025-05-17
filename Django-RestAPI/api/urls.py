from django.urls import path, include
from . import views
from rest_framework import routers

router= routers.DefaultRouter()
router.register('employeeview', views.employeeview, basename='employee')


urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/', views.studentdetailView),
    # path('employee/',views.employeeView.as_view()),
    path('employeemixinsdetail/<int:pk>/', views.employeemixinsdetail.as_view()),
    # path('employeemixins/', views.employeemixins.as_view()),
    path('employee/', views.GenericView.as_view()),
    path('employee/<int:pk>/', views.GenericDetail.as_view()),
    path('', include(router.urls)),
    path('blog/', views.blogView.as_view()),
    path('comment/', views.commentView.as_view()),
    path('blog/<int:pk>/', views.blogdetailView.as_view()),
    path('comment/<int:pk>/', views.commentdetailView.as_view()),
]
