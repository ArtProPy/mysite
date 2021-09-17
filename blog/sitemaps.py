""" Configuration sitemap """
from django.contrib.sitemaps import Sitemap

from blog.models import Post


class PostSitemap(Sitemap):
    """ Post sitemap """
    changefreq = 'weekly'
    priority = 0.9

    @staticmethod
    def items():
        """ Publish all posts of the site """
        return Post.published.all()

    @staticmethod
    def lastmod(obj):
        """ Lastmod """
        return obj.updated
