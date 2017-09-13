"""Advise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.views.static import serve

from Advises import views as advise_views
from gallery import views as gallery_views
from programs import views as programs_views

from Advise import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',advise_views.home,name="home"),
url(r'^base/$',advise_views.base, name="base"),
#url(r'^Advises/$',views.View_Advise, name="Advises"),
url(r'^Advises/$',advise_views.View_Advise, name="Advises"),
url(r'^gallery/$',gallery_views.gallery, name="Gallery"),
url(r'^signup/$', advise_views.signup, name="signup"),
url(r'^login/$', auth_view.login, name="login"),
url(r'^logout/$', auth_view.logout, name="logout"),
url(r'^likepost/$',advise_views.upatelikes, name="likepost"),
url(r'^search/$',advise_views.ajax_serach, name="search"),
url(r'^python/$', programs_views.Python_Code, name="Python"),
url(r'^java/$', programs_views.Java_Code, name="Java"),
url(r'^c/$', programs_views.C_Code, name="C"),
url(r'^select/$', programs_views.Selection, name="Selection"),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
