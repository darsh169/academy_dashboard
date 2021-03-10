from django.shortcuts import render,redirect
from app1.models import Academy
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def show(request):
	if request.method=='GET':
		data=Academy.objects.all()

	try:
		id=request.GET['id']
		entry=Academy.objects.get(id=id)
	except:
		entry=None
	return 	render(request,"index.html",{'data':data,'entry':entry})


def create(request):
	if request.method=='POST':
		name=request.POST['name']
		status=request.POST.get('status','')=='on'
		if not status:
			status=False
		price=int(request.POST['price'])
		players_per_court=int(request.POST['players_per_court'])

		Academy(name=name,status=status,price=price,players_per_court=players_per_court).save()
	return redirect('/show')


def delete(request,id):
	Academy.objects.filter(id=id).delete()
	return redirect('/show')

def update(request,id):
	name=request.POST['name']
	status=request.POST.get('status','')=='on'
	if not status:
		status=False
	price=int(request.POST['price'])
	players_per_court=int(request.POST['players_per_court'])
	record=Academy.objects.filter(id=id).update(name=name,status=status,price=price,players_per_court=players_per_court)
	
	return redirect('/show')
	# entry=Academy.objects.get(id=id)
	# data=Academy.objects.all()

	# return render(request,"index.html",{'data':data,'entry':entry})


