from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView
from .models import Flavour,Ingredient,CustomerSuggestion
from django.contrib import messages

from django.views.generic import ListView
from .models import Flavour  # Replace with your actual model name

class FlavorListView(ListView):
    model = Flavour
    template_name = 'myapp/flavour_list.html'  
    context_object_name = 'flavors'
    
    def get_queryset(self):
        queryset = Flavour.objects.filter(is_active=True)
        season_name = self.request.GET.get('season')
        
        if season_name:
            queryset = queryset.filter(season__name__iexact=season_name)
        
        return queryset
class IngredientListView(ListView):
    model = Ingredient
    temp_name = 'myapp/ingredient_list.html'
    context_object_name = 'ingredients'

class CustomerSuggestionCreateView(CreateView):
    model = CustomerSuggestion
    template_name = 'myapp/suggestion_form.html'
    fields = ['customer_name','flavour_name', 'description', 'allergies']
    success_url = '/'

