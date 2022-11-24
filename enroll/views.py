from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from .form import UserRegisterForm
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    form = UserRegisterForm
    stud= User.objects.all()

    context ={
        'form': form,
        'stud': stud,
    }
    return render(request,'enroll/home.html',context)

#save_data
@csrf_exempt
def save_data(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name= request.POST['name']  # name in Post is from ajax mydata
            email=request.POST['email']  # email in Post is from ajax mydata
            password=request.POST['password']  # password in Post is from ajax mydata

            if (sid==''):
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=sid, name=name, email=email, password=password)
            usr.save()
            stud=User.objects.values()
            #print(stud)
            student_data=list(stud)
            return JsonResponse({'status':'saved','student_data':student_data})
        else:
            return JsonResponse({'Status':0})

#delete_data
@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id=request.POST['sid']  # id in Post is from ajax mydata
        pi=User.objects.get(pk=id)
        print(id)
        pi.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status":0})

#edit_data
@csrf_exempt
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')  # id in Post is from ajax mydata
        print(id)
        student = User.objects.get(pk=id)
        student_data = {"id":student.id, "name":student.name,"email":student.email,"password":student.password}
        return JsonResponse(student_data)
