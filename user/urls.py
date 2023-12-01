from django.urls import path
from .views import user_login, registration, profile

app_name = 'user'

urlpatterns = [
    # path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
]
