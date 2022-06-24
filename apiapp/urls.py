
from django.urls import include, path
from rest_framework import routers
from apiapp import views

router = routers.DefaultRouter()
#router.register(r'studentapi', views.student_operations)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('mystudent',views.student_operations),
    path('studentupdate/<str:id>',views.update_student),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
