from django.shortcuts import render

def about(request):
    template_name = 'about.html'
    context = {}
    return render(request, template_name, context)

def rules(request):
    template_name = 'rules.html'
    context = {}
    return render(request, template_name, context)