from django.conf.urls import url 
from step2 import views

urlpatterns = [ 
	url(r'^about/',views.about, name='about'),
]
