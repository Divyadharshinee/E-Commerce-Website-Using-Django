from django.shortcuts import render, HttpResponse

# Create your views here.

tasks=[]

def dashboard(request):
    task_data = {}
    
    if request.POST:
        task = request.POST.get("task")
        assigned_to = request.POST.get("assigned_to")

        task_data["task"] = task
        task_data["assigned_to"] = assigned_to
        
        tasks.append(task_data)

    context = {
        "tasks":tasks
    }

    return render(request, "dashboard.html", context)

          