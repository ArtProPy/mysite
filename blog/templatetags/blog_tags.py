""" Configuration tags of the blog """
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

import markdown

from blog.models import Post

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    """ Markdown post output """
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_posts():
    """ Output count of the posts """
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_post(count=5):
    """ Output 5 of the oldest posts """
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_post': latest_post}


@register.inclusion_tag('blog/post/most_comment_posts.html')
def get_most_commented_posts(count=5):
    """ Output 5 of the most commented posts """
    most_commented_posts = Post.published.annotate(total_comments=Count('comments')).order_by(
        '-total_comments')[:count]
    return {'most_commented_posts': most_commented_posts}
