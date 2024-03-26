from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        
        task = Task(name=name, priority=priority)
        task.save()
        
    return render(request, 'myapp/add.html')