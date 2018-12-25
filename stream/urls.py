"""stream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from input import views


# from Slm.stream.input.views import list_manage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.admin_0),
    url(r'^index/$',views.index),
    url(r'^reptilian/login_action/$', views.login_action),
    url(r'^content_page/(\d+)/$',views.content_manage,name='content_manage'),#name=指向views里面
    url(r'^crawl/$',views.crawl_manage),
    url(r'^crawl_action/(\d+)/$',views.crawl_action),
    url(r'^newspaper/$',views.newspaper),
    url(r'^newspaper/(\d+)/$', views.newspaper,name='newspaper'),

    url(r'^crawl_save/(\d+)/$',views.crawl_save),
    url(r'^new_index/$',views.new_index),
    url(r'^album/$',views.album),
    url(r'^admin_0/$', views.admin_0),
    url(r'^reptilian/$',views.reptilian),
    url(r'^api_page/$',views.api_page),
    url(r'^comment/(\d+)/$', views.comment),

    # url(r'^api/',include('input.urls',namespace='input')),#配置具体接口的二级路径。
    url(r'^logout/$',views.logout),
    url(r'^cover/$', views.cover),
    url(r'^film/$',views.film),
    url(r'^cover2/$', views.cover2),
    # url(r'^cover2/(\d+)/$', views.cover2,name='cover2'),
]

handler404 = views.page_not_found
handler500 = views.page_error