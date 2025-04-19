from home import views
from django.urls import re_path as url

urlpatterns =[
     url('^$',views.homepage1),
     url('/predict',views.predict),
     url('/about',views.about),
     url('/firstaid',views.firstaid),
     url('/professionaltreatment',views.pt),
     url('/img',views.img),
     url('/hospregis',views.hospregis),
     url('/hospital_from',views.hospital_from),
     url('/hospital',views.nearhospi),
     url('/city',views.hospital_result),
     url('/me',views.aboutus),

]
