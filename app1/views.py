from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')



from .models import Loan

def addloan(request):

    if request.method == "POST":

        loan = Loan.objects.create(
            user=request.user,
            borrower_name=request.POST['borrower_name'],
            amount=request.POST['amount'],
            interest_rate=request.POST['interest_rate'],
            loan_date=request.POST['loan_date'],
            duration_months=request.POST['duration_months']
        )

        print("Saved Loan ID:", loan.id)

        return redirect('/')

    return render(request, 'addloan.html')


from django.contrib.auth import authenticate, login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(
                request,
                'login.html',
                {'error': 'Invalid Credentials'}
            )
    return render(request, 'login.html')