from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from spider_app.models import Douban


def spider(request):
    content = Douban.objects.all().values()
    return render(request, 'spider.html', {'content': content})


# @csrf_protect
def add(request):
    if request.method == 'POST':
        test1 = Douban(
            rank=request.POST.get('rank'),
            name=request.POST.get("name"),
            star=request.POST.get("star"),
            num=request.POST.get("num"),
            text=request.POST.get("text"),
            date=request.POST.get("date"),
            address=request.POST.get("address"),
        )
        test1.save()
        return HttpResponse("<p>数据添加成功！</p>")


def delete(request):
    if request.method == 'POST':
        base_id = request.POST.get('id')
        nameIndb = Douban.objects.filter(id=base_id).first()
        if nameIndb:
            nameIndb.delete()
            return HttpResponse(f'<p>{base_id}删除成功!</p>')
        else:
            return HttpResponse('<p>输入有误,值不存在')


def change(request):
    if request.method == 'POST':
        base_id = request.POST.get('id')
        nameIndb = Douban.objects.filter(id=base_id).first()
        if nameIndb:
            nameIndb.rank = request.POST.get('rank')
            nameIndb.name = request.POST.get('name')
            nameIndb.star = request.POST.get("star")
            nameIndb.num = request.POST.get("num")
            nameIndb.text = request.POST.get("text")
            nameIndb.date = request.POST.get("date")
            nameIndb.address = request.POST.get("address")
            nameIndb.save()
            return HttpResponse(f'<p>{base_id}修改成功!</p>')
        else:
            return HttpResponse(f'<p>输入有误,{base_id}不存在')


def select(request):
    if request.method == 'POST':
        base_id = request.POST.get('id')
        nameIndb = Douban.objects.filter(id=base_id).first()
        if nameIndb:
            return HttpResponse(f'<p>排名:{nameIndb.rank},'
                                f'名字{nameIndb.name},'
                                f' 星级评分:{nameIndb.star},'
                                f' 评论数{nameIndb.num},'
                                f' 描述:{nameIndb.text},'
                                f' 发行日期:{nameIndb.date},'
                                f' 发行国家:{nameIndb.address}</p>'
                                )
        else:
            return HttpResponse(f'<p>输入有误,{base_id}不存在')
