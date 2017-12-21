from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View, FormView, CreateView
from newsletter.forms import JoinForm 
# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'pages/home.html', {})
from .models import Page

class HomeView(SuccessMessageMixin, CreateView):
    template_name   = 'pages/home.html'
    form_class      = JoinForm
    success_url     = '/'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return 'Thank you for joining!' 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['page_obj'] = Page.objects.all().first()#order_by('?').first()
        return context


    # def form_clean(self, form):
    #     email = form.cleaned_data.get('email')
    #     return super().form_valid(form) #CreateView - will do all this stuff from this function for us, will create an item in database..