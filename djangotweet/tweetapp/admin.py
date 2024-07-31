from django.contrib import admin
from tweetapp.models import Tweet
#from . import models ikisinden biri
# Register your models here.

#özelleiştirme ile
class TweetAdmin(admin.ModelAdmin):
    fieldsets = [ # gruplandırma yapmaya yarar
        ('Message Group',{"fields":["message"]}),
        ('Nickname Group',{"fields":["nickname"]}),
    ]
    #fields = ['nickname','message']  # buradan sırası veya herhangi birini düzenlemeyi kaldırm yapılabilir

admin.site.register(Tweet,TweetAdmin)




#bu normali özelleştirmiceksek böyle kullanmamız yeterli
#admin.site.register(Tweet) #buşekilde app i bağladık
#ve eklediğimiz tweetler admin sayfasında artık gözükür
# ve görüntülediğimizde admin sayfasında,__str__ yaptığımız şekliyle gözükür

