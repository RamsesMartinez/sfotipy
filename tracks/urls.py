from django.conf.urls import url

from . import views
app_name = 'tracks'

urlpatterns = [
    url(r'^tracks/(?P<title>[\w\-]+)/', views.track_view, name='track_view'),

]
