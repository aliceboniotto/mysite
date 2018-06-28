from django.contrib import admin
from .models import Post #importo il post da models senza dover ricopiare tutta la classe
# Register your models here.


#il nostro post potrà essere visibile nella admin page
admin.site.register(Post)
