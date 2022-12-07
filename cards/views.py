from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView
from .models import Card
import random
from .form import CardCheckForm
# Create your views here.

class CardList(ListView):
    model=Card
    template_name="cards/card_list.html"
    
    #paginate_by=3 #not used here
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    
    #we specify a query-set to customize listing
    #if query set is not overriden here then all model
    #isntances will be retrieved from database
    queryset =Card.objects.all().order_by("box","-date_created")


class CardCreateView(CreateView):
    model=Card
    fields=["question","answer","box"]
    
    #if template_name is not override then a template 
    #with name modelNam_form.html must be created in templtes 
    
   # template_name="cards/card_form.html"
    success_url=reverse_lazy("card-create")
    
    
class CardUpdateView(CardCreateView,UpdateView):
    success_url=reverse_lazy("card-list")
   
    
class BoxView(CardList):
    
    template_name="cards/box.html"
    form_class=CardCheckForm
    #Note self.kwargs["box_num"]
    #is obtained from url routing 
    # path( "box/<int:box_num>" ... etc
    
    def get_queryset(self):
        return Card.objects.all().filter(box=self.kwargs["box_num"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"]=random.choice(self.object_list)
        return context
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])
        return redirect(request.META.get("HTTP_REFERER"))