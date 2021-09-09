""" Configuration sitemap """
from django.contrib.sitemaps import Sitemap

from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    @staticmethod
    def lastmod(obj):
        return obj.updated
