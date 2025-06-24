from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
# todoApp/views.py

def home(request):
    form = TodoForm(request.POST or None)

    if request.method == 'POST':
        # 1) Concluir (toggle)
        if 'toggle_id' in request.POST:
            todo = get_object_or_404(Todo, pk=request.POST['toggle_id'])
            todo.isCompleted = not todo.isCompleted
            todo.save()
            return redirect('home')

        # 2) Nova tarefa
        if form.is_valid():
            form.save()
            return redirect('home')

    # 3) carregar listas separadas
    pending   = Todo.objects.filter(isCompleted=False).order_by('-created_at')
    completed = Todo.objects.filter(isCompleted=True).order_by('-created_at')

    return render(request, 'home.html', {
        'form':      form,
        'pending':   pending,
        'completed': completed,
    })

   
            
def about(request):
    my_name = 'Joao Pedro'
    context = {'name':'Joao','age':20}
    return render(request,'about.html', context)


def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit.html', {'form': form,  'todo': todo})


def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    
    return render(request, 'delete.html', {
        'todo': todo,
    })
