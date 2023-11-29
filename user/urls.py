from django.urls import path
from .views import login_view,user_login,registration

app_name='user'

urlpatterns = [
    # path('', home, name='home'),
     path('login/',user_login , name='user_login'),
     path('registration/', registration, name='registration'),
    # path('userinfo/', user_info, name='userinfo'),
]