from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home,name='home'),
    path("team/",views.Team, name ="1_team"),
    path("pj_back/",views.Pj_Back, name ="1_back"),
    path("pj_effect/",views.Pj_Effect, name ="1_effect"),
    path("pj_db/",views.Pj_Db, name ="2_db"),
    path("pj_ending/",views.Pj_Ending, name ="2_ending"),
    path("pj_process/",views.Pj_Process, name ="2_process"),
    path("pj_predict/",views.Pj_Predict, name ="3_predict"),
    path("pj_review/",views.Pj_Review, name ="4_review"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)