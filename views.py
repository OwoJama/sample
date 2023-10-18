from django.shortcuts import render, redirect
from .forms import registerationForms

# Create your views here.


# def home(request):
#   return render(request, 'sample/dashboard.html')
def user_registeration(request):
    if request.method == 'POST':
        form = registerationForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('successful')

    else:
        form = registerationForms()

    return render(request, 'sample/dashboard.html', {'form': form})
