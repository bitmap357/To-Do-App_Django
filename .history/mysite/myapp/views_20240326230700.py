from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method == "POST":
        name = request.POST.get()
    return render(request, 'myapp/add.html')