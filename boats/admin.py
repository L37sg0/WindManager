from django.contrib import admin
from .models import Boat#, Answer

# Register your models here.
#class AnswerInLine(admin.TabularInline):
 #   model = Answer
  #  extra = 4
    

class BoatAdmin(admin.ModelAdmin):
    fieldsets = [
        #('id:',               {'fields':['id']}),
        ('Име:', {'fields':['name']}),
        ('Собственик:', {'fields':['owner_id']}),
        #('Дата:', {'fields':['date_made']}),
        ('Наемна цена:', {'fields':['rental_price']}),
    ]
    #inlines = [AnswerInLine]
    list_display = ('id','name', 'owner_id','rental_price')#'date_made','rental_price')
    list_filter = ['id']
    search_fields = ['name', 'id', 'owner_id', 'rental_price']

admin.site.register(Boat, BoatAdmin)