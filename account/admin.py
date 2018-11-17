from django.contrib import admin

# Register your models here.
from account.models import Doctor,User,Admin,OrdinaryUser,Symptom,Data

admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(OrdinaryUser)
admin.site.register(Admin)

admin.site.register(Symptom)

admin.site.register(Data)