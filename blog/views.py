from django.shortcuts import render


posts = [
    {
        'author' : 'Joseph, sam',
        'title' : 'Blog post 1',
        'content' : 'This is my first django web app code',
        'date_posted' : 'Feb 20 2020',
        'country' : 'Kenya'
    },
    
    {
        'author' : 'William',
        'title' : 'Blog post 2',
        'content' : 'This is another django web app code',
        'date_posted' : 'Feb 16 2020',
        'country' : 'Rwanda'
    },
    
    {
        'author' : 'Winnie Achieng',
        'title' : 'Blog post 3',
        'content' : 'This is my first django web app code, learning and learning',
        'date_posted' : 'Feb 28 2020',
        'country' : 'Ethiopia'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About us'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact us'})