from django.urls import path
from .views import login_view,user_login

app_name='user'

urlpatterns = [
    # path('', home, name='home'),
     path('login/',user_login , name='user_login'),
    # path('signup/', signup, name='signup'),
    # path('userinfo/', user_info, name='userinfo'),
]
