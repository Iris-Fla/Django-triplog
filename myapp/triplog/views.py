from django.shortcuts import render

def index(request):
    context = {
        'title':'旅行の記録 - 一覧画面',
    }
    return render(request, 'triplog/index.html',context)