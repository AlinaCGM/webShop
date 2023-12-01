from django.urls import path
from .views import user_login, registration, profile,user_logout

app_name = 'user'

urlpatterns = [
    # path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='user_logout'),
]
