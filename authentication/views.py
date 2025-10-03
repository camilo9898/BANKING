#from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
#def index(request):
#    return HttpResponse(" - - - - ¡This is my first view! - - - - ")
#def country(request):
#    return HttpResponse(" - - - - ¡COUNTRY! - - - - ")
#def city(request):
#    return HttpResponse(" - - - - ¡CITY! - - - - ")
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Country
from .forms import CountryForm
def country_list(request):
 countries = Country.objects.all().order_by('name')
 return render(request, 'authentication_app/country_list.html', {'countries': countries})
def country_edit(request, pk):
 country = get_object_or_404(Country, pk=pk)
 if request.method == 'POST':
   form = CountryForm(request.POST, instance=country)
 if form.is_valid():
   form.save()
 messages.success(request, 'País actualizado correctamente.')
 return redirect('country_list')
 #else:
 form = CountryForm(instance=country)
 return render(request, 'authentication_app/country_form.html', {'form': form, 'country': country})