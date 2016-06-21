from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^randomnote/$', views.shuffle, name='random'),
    url(r'^createnote/$', views.note_new, name='note_new'),
    url(r'^(?P<pk>\d+)/delete$', views.note_delete, name="note_delete"),
    url(r'^(?P<note_pk>\d+)/edit$', views.note_edit, name="note_edit"),
]
