from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Page
from facebook.models import Comment


# Create your views here.


def play(request):
    return render(request, 'play.html')


count = 0


def play2(request):
    choidogeun = '최도근'

    global count
    count = count + 1
    return render(request, 'play2.html', {'name': choidogeun, 'cnt': count})


def help(request):
    return render(request, 'help.html')


def warn(request):
    return render(request, 'warn.html')


def newsfeed(request):
    articles = Article.objects.all()

    return render(request, 'newsfeed.html', {'articles': articles})


def detailfeed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        Comment.objects.create(
            article = article,
            author = request.POST['nickname'],
            password = request.POST.get('password'),
            text = request.POST.get('reply')
        )

        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detailfeed.html', {'feed': article})


def pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html', {'pages': pages})


def new_feed(request):
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'] + " - 추신: 감사합니다.",
                password=request.POST['password']
        )

        return redirect(f'/feed/{ new_article.pk }')

    return render(request, 'new_feed.html')


def new_page(request):
    if request.method == 'POST':
        new_page = Page.objects.create(
            master=request.POST['master'],
            name=request.POST['name'],
            text=request.POST['content'],
            category=request.POST['category']
        )

        return redirect('/pages/')

    return render(request, 'new_page.html')


def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail/')

    return render(request, 'edit_feed.html', {'feed': article})


def edit_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == "POST":
        page.master = request.POST['master']
        page.name = request.POST['name']
        page.text = request.POST['text']
        page.category = request.POST['category']
        page.save()
        return redirect('/pages/')

    return render(request, 'edit_page.html', {'page': page})


def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')

        else:
            return redirect('/fail/')

    return render(request, 'remove_feed.html', {'feed': article})


def remove_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.delete()
        return redirect('/pages/')

    return render(request, 'remove_page.html',{'page': page})



def fail(request):
    return render(request, 'fail.html')


def new_page(request):
    return render(request, 'new_page.html')





