from django.conf.urls import url,include
from . import views


urlpatterns = [
    
    url('signup/', views.signup, name='signup'),
  
]