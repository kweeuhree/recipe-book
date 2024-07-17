from django.shortcuts import redirect


def home_page(request):
    return redirect('https://your-s3-bucket-url.s3.amazonaws.com/index.html')
