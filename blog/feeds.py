""" News feeds """
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from blog.models import Post


class LatestPostsFeed(Feed):
    """ Getting last posts feed """
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    @staticmethod
    def items():
        """ Out last 5 posts  """
        return Post.published.all()[:5]

    @staticmethod
    def item_title(item):
        return item.title

    @staticmethod
    def item_description(item):
        return truncatewords(item.body, 30)
