# from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf.urls import url

from . import feeds
from . import sitemap
from . import views

sitemaps = {'static': sitemap.VideoViewSitemap, }

urlpatterns = (
    url(r'^$', views.home, name='home'),
    url(r'^channel/(?P<slug>\w+)', views.channel, name='channel'),
    url(r'^detail/(?P<id>\d+)', views.detail, name='detail'),
    url(r'^player/(?P<id>\d+)', views.player, name='player'),
    url(r'^detail/(?P<id>\d+\.html)', views.detail, name='detail'),
    url(r'^browse', views.browse, name='browse'),
    url(r'^live', views.live, name='live'),
    # url(r'^live|\.html', views.live, name='live'),

    # url(r'^tags/(?P<name>[\w|\s]+)', views.tags, name='tags'),
    # url(r'^slide/(?P<swith>\w+)/(?P<id>\d+)', views.slide, name='slide'),
    # url(r'^waterfall/(?P<id>\d+)', views.waterfall, name='slide'),
    # url(r'^new.html', views.new, name='new'),
    # url(r'^rec.html', views.rec, name='rec'),
    # url(r'^hot.html', views.hot, name='hot'),
    url(r'^feed/rss\.xml$', feeds.RSS(), name='feed_rss_xml'),
    # url(r'^sitemap\.xml', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
