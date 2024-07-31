from django.shortcuts import render,redirect
from . import models
from django.urls import reverse,reverse_lazy #reverse den farkı sadece buraya ulaşıldığında çalışır reverse her uygulama başladğında çalışır buda sadece kayıt olmasına rağmen her seferinde çalışması gereken birşey değil
from tweetapp.forms import AddTweetForm,AddTweetModelForm #django form kısmı için ve modelform için
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm #kullanıcı oluşturma formu
from django.views.generic import CreateView # buda üsttekini kullanabilmek için

# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render(request, 'tweetapp/listtweet.html',context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST: #request postsa çalışacak kısım 
        #nickname = request.POST["nickname"] #buranın içindeki yazılar html de  artık ihtiyacımız yok
        message = request.POST["message"]  #name olarak eklediğimiz yerlerin ismi
        #tweet = models.Tweet(nickname,message)
        #tweet.save()    #db e kaydettik
        models.Tweet.objects.create(username=request.user,message=message) #nickname=nickname vardı önceden
        #şeklinde de kaydedebiliriz db e
        return redirect(reverse('tweetapp:listtweet'))   #diğer html e yönlendirdik gönderince
    else: #burası getle çalıştığından else yazsak olur
        return render(request, 'tweetapp/addtweet.html')
    

def addtweetbyform(request):  #djangonun otomatik formlarıyla yaptık html kodu çok az yazdık 2.form yoludur
    if request.method == "POST":#üsttekinin 2.türü
        form = AddTweetForm(request.POST)
        if form.is_valid():  #form geçerli değerler aldıysa demek
            nickname = form.cleaned_data["nickname_input"] #forms.py de giriş yapılan alanların ismi
            message = form.cleaned_data["message_input"]#yani alınan değerleri yine html e yönlendirdik
            models.Tweet.objects.create(nickname=nickname,message=message) #models deki veri tabanına kaydettik
            return redirect(reverse('tweetapp:listtweet')) #button tıklanınca ana sayfaya yönlendirdik
        else:
            print("error in form!") #olurda form hatalı çalışırsa 
            return render(request,'tweetapp/addtweetbyform.html',context={"form":form})
    else:
        form = AddTweetForm()
        return render(request,'tweetapp/addtweetbyform.html',context={"form":form})
    

def addtweetbymodelform(request): #3.form yoludur
    if request.method == "POST": #üstten kopyaladık
        form = AddTweetModelForm(request.POST)
        if form.is_valid():  
            nickname = form.cleaned_data["nickname"] #forms.py de bu şekilde kayıtlı
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname,message=message) 
            return redirect(reverse('tweetapp:listtweet')) 
        else:
            print("error in form!") 
            return render(request,'tweetapp/addtweetbymodelform.html',context={"form":form})
    else:
        form = AddTweetModelForm()
        return render(request,'tweetapp/addtweetbymodelform.html',context={"form":form})
    
@login_required
def deletetweet(request,id):  #tweet silme özelliği
    tweet = models.Tweet.objects.get(pk=id) #güncel tweet i aldık
    if request.user == tweet.username:   # güvenlik önlemi için bu request i yapan kullanıcı tweet in kullanıcısa eşit sil işlemini yaptık
        models.Tweet.objects.filter(id=id).delete()  #burada tweet.delete() de yapabilirdik
        return redirect('tweetapp:listtweet')  # sildikten sonra sayfa yönlendirmesi

class SignUpView(CreateView):
    form_class = UserCreationForm  #burası birebir olmalı hangi formu kullanacağımız
    success_url = reverse_lazy("login")  #başarılı olursa nereye yönlendirileceği
    template_name = "registration/signup.html"  #hangi templete bağlı olduğunu belirttik tweetapp de yapabilirdik