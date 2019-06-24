"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from Main import settings
from RoboBeast.views import *


urlpatterns = [
    url(r'^logout/$', logout_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api/', include('rest_auth.urls')),

    url(r'^get_user_profile_list/', UserProfileListAPIView.as_view()),
    url(r'^get_update_user_profile_list/(?P<user_id>[\w-]+)/edit/$', UserProfileRetrieveAPIView.as_view()),
    url(r'^post_user_profile_list/', UserProfileCreateAPIView.as_view()),

    # url(r'^form/$', Form),
    # url(r'^upload/$', Upload),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns

