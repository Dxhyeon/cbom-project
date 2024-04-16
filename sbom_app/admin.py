from django.contrib import admin
from .models import SearcheData, ParsingCveData, SbomVulData, CveData, SbomAppSbomData


# Register your models here.
admin.site.register(SearcheData)
admin.site.register(ParsingCveData)
admin.site.register(CveData)
admin.site.register(SbomAppSbomData)
admin.site.register(SbomVulData)