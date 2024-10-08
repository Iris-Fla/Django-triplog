from django.shortcuts import render
from triplog.models import Triplog

def index(request):
    all_data = Triplog.objects.all()
    context = {
        'title':'旅行の記録 - 一覧画面',
        'all_data':all_data,
    }
    return render(request, 'triplog/index.html',context)