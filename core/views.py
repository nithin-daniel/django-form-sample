from django.shortcuts import render
from .forms import mainform
from django.shortcuts import redirect
from .models import form
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        # create a form instance and populate it with data from the request:
        form = mainform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = mainform()
    return render(request, 'index.html', {'form': form})



def success(request):
    return render(request,'success.html')


def form_admin(request):
    data = form.objects.all()
    context = {'data':data}
    return render(request,'admin.html',context)