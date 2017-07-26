from django.conf.urls import url
from .views import IndexView, ProView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^albums/$', ProView.as_view(), name='albumes'),
    # url(r'^albums/(?P<slug>[-\w]+)/$', ProView.as_view(), name='in_album'),
]
