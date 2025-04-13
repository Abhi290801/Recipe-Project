from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):

    peoples = [
        {'name': 'Abhijeet Gupta','age': 26},
        {'name': 'Rohan Sharma','age': 17},
        {'name': 'Vicky kaushal','age': 24},
        {'name': 'Dipanshu Chaurasiya','age': 16},
        {'name': 'Sandeep','age': 20}
    ]

    # The below for is for printing in console
    # for people in peoples:
    #     print(people)
    
    vegetables = ['Pumpkin','Tomato','Potato']

    return render(request, "home/index.html", context = {'page':'Django Learning','peoples':peoples,'vegetables' : vegetables})

    # return HttpResponse("""<h1>Hey I am a Django Server.</h1>
    #     <p>Hey this is coming form Django server</p>
    #     <hr>
    #     <h3>Hope you are loving it :)</h3>
    # """)
def about(request):
    context = {'page':'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page':'Contact'}
    return render(request, "home/contact.html",context)
    

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1> Hey this is a success Page </h1>")