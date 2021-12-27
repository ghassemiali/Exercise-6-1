from django.shortcuts import render

def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def about_view(request):
    return render(request, 'website/about.html')

def elements_view(request):
    return render(request, 'website/elements.html')

def test_view(request):
    context = {'fname': 'Ali', 'lname': 'Ghassemi'}
    return render(request, 'test.html', context)

