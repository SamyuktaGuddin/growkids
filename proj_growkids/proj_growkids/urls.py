"""proj_growkids URL Configuration

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
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from kids import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
url(r'^$', views.showhome, name='showhome'),
url('^explfrm', views.explfrm, name='explfrm'),
url('^profilefrm', views.profilefrm, name='profilefrm'),
url('^bspfrm', views.bspfrm, name='bspfrm'),
url('^regfrm', views.regfrm, name='regfrm'),
url('^logcheck', views.logcheck, name='logcheck'),
url('^changepass', views.changepass, name='changepass'),
url('^showstudent', views.showstudent, name='showstudent'),
url('^makepay', views.makepay, name='makepay'),
url('^showabout', views.showabout, name='showabout'),

url('^showcontact', views.showcontact, name='showcontact'),

url('^showenroll', views.showenroll, name='showenroll'),
url('^showtrainingdetails', views.showtrainingdetails, name='showtrainingdetails'),
url('^showtrainerdetails', views.showtrainerdetails, name='showtrainerdetails'),
url('^showpayment', views.showpayment, name='showpayment'),
url('^inserttrainingdetails', views.inserttrainingdetails, name='inserttrainingdetails'),
url('^showtrainerdetailsstud', views.showtrainerdetailsstud, name='showtrainerdetailsstud'),

url('^showstdenttrainer', views.showstdenttrainer, name='showstdenttrainer'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
