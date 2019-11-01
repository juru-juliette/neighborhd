from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^accounts/profile/(\d+)', views.profile, name='profile'),
    url(r'^accounts/edit_profile/', views.edit_profile, name='edit_profile'),
]