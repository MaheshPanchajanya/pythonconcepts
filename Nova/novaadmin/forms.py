from  django.forms import ModelForm
from django.urls.conf import include
from  users.models import Extendmyuser,Empuser
from novacustomermodule.models import Company

class Updatefrom(ModelForm):
    class Meta:
        model = Extendmyuser
        fields = '__all__'
        exclude = ['companyname']
        

class  Clients(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class Manage(ModelForm):
    class Meta:
        model = Empuser
        fields = '__all__'
        
        
