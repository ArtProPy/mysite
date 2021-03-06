""" A document with all the blog views """
from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

from taggit.models import Tag

from blog.forms import EmailPostForm, CommentForm, SearchForm
from blog.models import Post


def post_list(request, tag_slug=None):
    """ Displaying a page with posts """
    search_query = request.GET.get('search')
    print(request)
    if search_query:
        object_list = Post.published.filter(Q(title__icontains=search_query) |
                                            Q(body__icontains=search_query))
    else:
        object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        assert isinstance(page, object)
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    """ Detailed display of the page with the post """
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # Пользователь отправил комментарий
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создание комментария без сохранения в БД
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    # Получение тегов статьи
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_post = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    # Получение 4 похожих статей по тегам
    similar_post = similar_post.annotate(same_tags=Count('tags')).order_by(
        '-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.html',
                  {'post': post, 'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_post': similar_post})


def post_search(request):
    """ Displaying the post search page """
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)
    return render(request, 'blog/post/search.html',
                  {'form': form, 'query': query, 'results': results})


def post_share(request, post_id):
    """ Displaying the share post page """
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Форма была отправлена на сохранение
        form = EmailPostForm(request.POST)
        if form.is_valid():
            form_info = form.cleaned_data
            # Отправка электронной почты
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{form_info["name"]} ({form_info["email"]}) recommends you ' \
                      f'reading "{post.title}"'
            message = f'Read "{post.title}" at {post_url}\n\n{form_info["name"]}\'' \
                      f's comments:\n\n{form_info["comment"]}'
            send_mail(subject, message, form_info['email'], [form_info['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',
                  {'post': post, 'form': form, 'sent': sent})
