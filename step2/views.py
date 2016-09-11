from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from .models import Book
# Create your views here.


def view_stuff(request):
    context_dict={'boldmessage': Book.objects.all() }
    return render(request,'step2/view_stuff.html',context=context_dict)
    
    
    
    
    
    
def about(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            q= Book(book_name=form.cleaned_data['book_name'],price=form.cleaned_data['price'],user=form.cleaned_data['user'],phone=form.cleaned_data['phone'])
            q.save()
            return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        user = request.user

    return render(request, 'step2/welcome.html', {'form': form, 'user':user})