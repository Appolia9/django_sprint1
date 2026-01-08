from django.shortcuts import render

def about(request):
    template_name = 'pages/about.html'
    context = {}
    return render(request, template_name, context)

def rules(request):
    template_name = 'pages/rules.html'
    context = {}
    return render(request, template_name, context)