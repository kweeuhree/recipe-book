from django.shortcuts import redirect


def home_page(request):
    return redirect('http://django-react-bucket.s3.amazonaws.com/index.html')
