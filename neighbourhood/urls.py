from django.conf.urls import url
from . import views



urlpatterns=[
    # url(r'^$',PostListView.as_view(),name='home'),
    # url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
    # url(r'^signout/$', views.signout, name='signout'),
    # url(r'^search/',views.search_results, name='search_results'),

]
# urlpatterns = format_suffix_patterns(urlpatterns)

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)