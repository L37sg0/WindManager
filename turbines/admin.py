from django.contrib import admin
from .models import Turbine, Repair, Technician, TechGroup#, Answer

# Register your models here.
#class AnswerInLine(admin.TabularInline):
 #   model = Answer
  #  extra = 4
    

class TurbineName(admin.ModelAdmin):
    fieldsets = [
        ('Име на парк:', {'fields':['park_name']}),
        ('Диспечерско име:', {'fields':['disp_name']}),
        ('Име на фирма:', {'fields':['firm_name']}),
        ('Вид турбина:', {'fields':['turbine_type']}),
        ('Контрол:', {'fields':['control_type']}),
        #('Поддръжка от:', {'fields':['supported_by']}),
        ('Мощност на турбина(MW):', {'fields':['turbine_power']}),


        ('Име на турбина:', {'fields':['turbine_id']}),
        ('Извод:', {'fields':['output_name']}),
        ('Подстанция:', {'fields':['station_name']}),
        ('ГРУ:', {'fields':['gru_name']}),
        ('СОТ:', {'fields':['sot_firm']}),
        ('Обект СОТ:', {'fields':['sot_name']}),


        ('Прогнозираща компания:', {'fields':['forecaster']}),
        ('Интернет доставчик:', {'fields':['isp_name']}),
    ]
    #inlines = [AnswerInLine]
    list_display = ('turbine_id', 'park_name', 'disp_name', 'firm_name', 'turbine_type', 'control_type', #'supported_by',
    'turbine_power', 'output_name', 'station_name', 'gru_name',
    'sot_firm', 'sot_name', 'forecaster', 'isp_name')
    list_filter = ['turbine_id']
    search_fields = ['id', 'park_name', 'disp_name', 'firm_name', 'turbine_type', 'control_type', #'supported_by',
    'turbine_power', 'turbine_id', 'output_name', 'station_name', 'gru_name',
    'sot_firm', 'sot_name', 'forecaster', 'isp_name']

class RepairEvent(admin.ModelAdmin):
    fieldsets = [
        ('Турбина', {'fields':['turbine']}),
        ('Дата:', {'fields':['repair_date']}),
        ('Описание:', {'fields':['repair_type']}),
        ('Техник:', {'fields':['technician']}),
        #('Техник2:', {'fields':['technician_second']}),
    ]
    #inlines = [AnswerInLine]
    list_display = ('turbine', 'repair_date', 'repair_type', 'technician')#, 'technician_second')
    list_filter = ['repair_date']
    search_fields = ['turbine__turbine_id', 'repair_date', 'repair_type', 'technician__technician_name']#, 'technician_second']

class TechnicianName(admin.ModelAdmin):
    fieldsets = [
        ('Име:', {'fields':['technician_name']}),
        ('Квалификация:', {'fields':['technician_techgroup']}),
        #('Техник2:', {'fields':['technician_second']}),
    ]
    #inlines = [AnswerInLine]
    list_display = ('technician_name', 'technician_techgroup')
    list_filter = ['technician_techgroup']
    search_fields = [('technician_name', 'technician_techgroup')]

class TechGroupName(admin.ModelAdmin):
    fieldsets = [
        ('Работна група:', {'fields':['techgroup_name']}),
    ]
    #inlines = [AnswerInLine]
    list_display = ('techgroup_name',)
    list_filter = ['techgroup_name']
    search_fields = [('techgroup_name')]

admin.site.register(Turbine, TurbineName)
admin.site.register(Repair, RepairEvent)
admin.site.register(Technician, TechnicianName)
admin.site.register(TechGroup, TechGroupName)