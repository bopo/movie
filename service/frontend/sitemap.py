from django.contrib import sitemaps

from .models import Video


class VideoViewSitemap(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Video.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
