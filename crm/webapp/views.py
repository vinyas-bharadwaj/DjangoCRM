from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Record


# Homepage
def home(request): 
  return render(request, 'webapp/index.html')

# Register user
def register(request):
  
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)

    if form.is_valid():
      form.save()

      messages.success(request, "Account created successfully")

      return redirect('login')

  context = {'form': form}

  return render(request, 'webapp/register.html', context=context)

# Login user
def my_login(request):
  
  form = LoginForm()

  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)

    if form.is_valid():

      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)

      if user is not None:
        auth.login(request, user)

        messages.success(request, "login success")

        return redirect('dashboard')
  
  context = {'form': form}

  return render(request, 'webapp/my-login.html', context=context)

# Dashboard view
@login_required(login_url='login')
def dashboard(request):
  my_records = Record.objects.all()

  context = {'records': my_records}

  return render(request, 'webapp/dashboard.html', context=context)

# Create a record
@login_required(login_url='login')
def create_record(request):
  
  form = AddRecordForm()

  if request.method == 'POST':
    form = AddRecordForm(request.POST)

    if form.is_valid():
      form.save()

      messages.success(request, "Record created successfully")

      return redirect('dashboard')
    
  context = {'form': form}

  return render(request, 'webapp/create-record.html', context=context)

# Update a record
@login_required(login_url='login')
def update_record(request, pk):
  
  record = Record.objects.get(id=pk)
  form = UpdateRecordForm(instance=record)

  if request.method == 'POST':
    form = UpdateRecordForm(request.POST, instance=record)

    if form.is_valid():
      form.save()

      messages.success(request, "Record updated successfully")

      return redirect('dashboard')
    
  context = {'form': form, 'record': record}

  return render(request, 'webapp/update-record.html', context=context)

# Read/View a singular record
@login_required(login_url='login')
def read_record(request, pk):
   
   all_records = Record.objects.get(id=pk)

   context = {'record': all_records}

   return render(request, 'webapp/view-record.html', context=context)

# Delete a singular record
@login_required(login_url='login')
def delete_record(request, pk):

  record = Record.objects.get(id=pk)

  record.delete()

  messages.success(request, "Record deleted successfully")

  return redirect('dashboard')


# Logout user
@login_required(login_url='login')
def user_logout(request):

  auth.logout(request)

  messages.success(request, "logout success")

  return redirect('login')