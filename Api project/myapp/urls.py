
from django.urls import path
from myapp import views


urlpatterns = [
    		path('getemployees/<str:name>/<str:mail>', views.getemployees),
    		path('face_api', views.face_api),
    		path('update/<int:ck>/<str:nm>/<str:em>', views.update),
    		path('delete/<int:ck>', views.delete),
	]