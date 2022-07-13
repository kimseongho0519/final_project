from django.shortcuts import render
from .models import tour_data
#from .models import naver_list

def Home(request):
    return render(request, 'main/home.html')

def Team(request):
    return render(request, 'main/1_team.html')

def Pj_Back(request):
    return render(request, 'main/1_back.html')

def Pj_Effect(request):
    return render(request, 'main/1_effect.html')

def Pj_Db(request):
    return render(request, 'main/2_db.html')
    
def Pj_Ending(request):
    return render(request, 'main/2_ending.html')

def Pj_Process(request):
    datas = tour_data.objects.all()
    # print(datas)
    return render(request, 'main/2_process.html', {"datas":datas})
    

# def Pj_Process(request):
#     datas = tour_data.objects.all()
#     return render(request, 'main/index.html', {"datas":datas})

def Pj_Predict(request):
    return render(request, 'main/3_predict.html')

def Pj_Review(request):
    return render(request, 'main/4_review.html')




# def naver_list(requests):
#     #db에서 데이터 query해서 오기
#     datas = naver_list.objects.all().order_by("-created_at")
#     #print(data)
#     return render(requests, 'main/naver_list.html', {"datas":datas})








# Create your views here.
