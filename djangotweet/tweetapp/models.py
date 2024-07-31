from django.db import models
from django.contrib.auth.models import User # burada kullanıcın username e ulaşmak için

# Create your models here.

class Tweet(models.Model):
    #nickname = models.CharField(max_length=50) uygulamada kayıt olduktan sonra artık user name girmeye gerek yok kayıt olma işlemini ekledikten sonra bu kısmı kaldırdık
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #burada foreignkey ile user modeline eriştik ondelete ise kullanıcı silinirse tweetlere nolacak karar verir silinir yaptık ve sonradan eklediğimiz için null ekledik önceki kullanıcılara boşluk ataması için başta eklesek gerek olmazdı
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Tweet user: {self.username} message: {self.message}"
        #return f"Tweet nick: {self.nickname} message: {self.message}" nickname varken ki hali
