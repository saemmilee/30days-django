from django.shortcuts import render

def index(request):
    """
    main 화면으로
    """
    return render(request, 'mainPage.html')
