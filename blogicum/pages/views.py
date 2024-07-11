from django.shortcuts import render


# Create your views here.
def about(requests):
    return render(requests, 'pages/about.html')


def rules(requests):
    return render(requests, 'pages/rules.html')
