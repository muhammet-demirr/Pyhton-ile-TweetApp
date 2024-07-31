from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'), #siteadı/tweetapp/
    #burda tweetapp e girildiğinde ilk açılacak sayfayı listtweet olarak seçtik
    path('addtweet/',views.addtweet,name='addtweet'),     #siteadı/tweetapp/apptweet 
    path('addtweetbyform',views.addtweetbyform,name='addtweetbyform'), #siteadı/tweetapp/addtweetbyform
    path('addtweetbymodelform',views.addtweetbymodelform,name='addtweetbymodelform'),#siteadı/tweetapp/addtweetbymodelform
    path('signup/',views.SignUpView.as_view(),name="signup"),  #SignUpView.as_view() şeklinde görünüre çeviririz class olduğu için   
    path("deletetweet/<int:id>",views.deletetweet,name="deletetweet"), # silme id siyle beraber aldık 
] 