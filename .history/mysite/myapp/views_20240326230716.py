from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = re
    return render(request, 'myapp/add.html')