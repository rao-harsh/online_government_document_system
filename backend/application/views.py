from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,IncomeForm,NonCreamyLayerForm
from . import models


# Create your views here.
def register(request):
    if request.method == "POST":
        user = models.CustomUser(email=request.POST["email"],first_name=request.POST["first_name"],last_name=request.POST["last_name"],contact=request.POST["Contact"],password=request.POST["Password"])
        try:
            user.set_password(user.password)
            user.save()
            return redirect("login_view")
        except Exception as e:
            return render(request,"register.html",{"error_message":"You're already registered so pls login sucker"})
    return render(request,"register.html")

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect("home")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            next_page = form.data["next"]
            
            user = authenticate(username=username,password=password)
            print(user.role)
            if user is not None:
                login(request,user)
                print(request.user.pk)
                if request.user.role == "admin":
                    return redirect("government-officer-panel")
                else:
                    if next_page != "None" and next_page != "" and next_page is not None:
                        return redirect(next_page)
                    else:
                        return redirect("home")
            else:
                return render(request,"login.html",{"error_message":"Invalid Username or password"})
        else:
            return render(request,"login.html",{"error_message":form.errors})
    else:
        next_page = request.GET.get("next")
    return render(request,"login.html",{"next":next_page})

def contact_us(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def required_income_certificate_docs(request):
    return render(request,"required_docs_income.html")

def required_ncl_docs(request):
    return render(request,"required_docs_ncl.html")

@login_required
def income_certificate(request):
    if request.method == "POST":
        form = IncomeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/income-certificate-form/?id={0}".format(request.user.pk))
        else:
            print(form.errors)
            return render(request,"income_certificate.html",{"error_message":form.errors})
    return render(request,"income_certificate.html")

@login_required
def non_creamy_layer(request):
    if request.method == "POST":
        form = NonCreamyLayerForm(request.POST,request.FILES)
        if form.is_Valid():
            form.save()
            return redirect("non-creamy-layer-form/?id={0}".format(request.user.pk))
        else:
            print(form.errors)
    return render(request,"non_creamy_layer.html")

@login_required
def print_non_creamy_layer(request):
    print(request.GET['id'])
    return render(request,"printing_data.html")

@login_required
def print_income(request):
    print(request.GET['id'])
    income_form = models.Income.objects.get(user=request.GET["id"])
    print(income_form)
    return render(request,"printing_data.html",{"income_form":income_form})

@login_required
def government_officer_panel(request):
    if request.user.role == "admin":
        return render(request,"government-officer-panel.html")
    else:
        return render(request,"login.html",{"error_message":"You're very chalak bro but i'm your fuckin' daddy sucker"})