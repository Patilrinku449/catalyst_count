


from django.contrib.auth.models import User
# from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
import os
from .models import File
import csv
# ---------working code--------------
# def datatable(request):
#     csv_data=[]
#     header = request.POST.getlist('header')  # Get the column names from the request
#     try:
#         with open('data/companies_sorted.csv', 'r',encoding="utf-8") as csv_file:
#             csvreader=csv.reader(csv_file)
#             for row in csvreader:
#                 csv_data.append(row)
#     except FileNotFoundError:
#         csv_data=[['File not found error']]
#
#     return render(request, 'query.html', {'header': header, 'csv_data': csv_data})










import csv

import csv
from collections import defaultdict

import csv
from collections import defaultdict

def datatable(request):
    header = ['Keyword', 'Industry', 'Year Founded', 'City', 'State', 'Country', 'Employees (From)', 'Employees (To)']  # Column names
    filters = {key: request.POST.get(key) for key in header}  # Get the filters from the request
    csv_data = []
    record_count = 0
    options = defaultdict(set)  # To store the unique values for each column
    try:
        with open('data/companies_sorted.csv', 'r', encoding="utf-8") as csv_file:
            csvreader = csv.reader(csv_file)
            for row in csvreader:
                if len(row) != len(header):
                    continue  # Skip rows that don't have the same number of elements as header
                if all(cell == filters[header[i]] for i, cell in enumerate(row) if filters[header[i]]):
                    csv_data.append(row)
                    record_count += 1
                for i, cell in enumerate(row):
                    if header[i] in options and isinstance(cell, collections.Hashable):
                        options[header[i]].add(cell)  # Add the cell value to the set of options for the corresponding column
    except FileNotFoundError:
        csv_data = [['File not found error']]

    return render(request, 'query.html', {'header': header, 'csv_data': csv_data, 'record_count': record_count, 'options': options})




def index(request):
    files = File.objects.filter(name='companaies.csv')

    # Check the number of results

    if request.method == 'POST':
        file = request.FILES['file'].read()
        fileName= request.POST['filename']
        existingPath = request.POST['existingPath']
        end = request.POST['end']
        nextSlice = request.POST['nextSlice']

        if file=="" or fileName=="" or existingPath=="" or end=="" or nextSlice=="":
            res = JsonResponse({'data':'Invalid Request'})
            return res
        else:
            if existingPath == 'null':
                path = 'data/' + fileName
                with open(path, 'wb+') as destination:
                    destination.write(file)
                FileFolder = File()
                FileFolder.existingPath = fileName
                FileFolder.eof = end
                FileFolder.name = fileName
                FileFolder.save()
                if int(end):
                    res = JsonResponse({'data':'Uploaded Successfully','existingPath': fileName})
                else:
                    res = JsonResponse({'existingPath': fileName})
                return res


            else:
                path = 'data/' + existingPath
                model_id = File.objects.filter(existingPath=existingPath).first()

                if model_id is not None:
                    if model_id.name == fileName:
                        if not model_id.eof:
                            with open(path, 'ab+') as destination:
                                destination.write(file)
                            if int(end):
                                model_id.eof = int(end)
                                model_id.save()
                                res = JsonResponse({'data':'Uploaded Successfully','existingPath':model_id.existingPath})
                            else:
                                res = JsonResponse({'existingPath':model_id.existingPath})
                            return res
                        else:
                            res = JsonResponse({'data':'EOF found. Invalid request'})
                            return res
                else:
                    res = JsonResponse({'data':'No such file exists in the existingPath'})
                    return res

    return render(request, 'upload.html')# from django.shortcuts import render

def admin_users(request):
    users = User.objects.filter(is_staff=True)
    return render(request, 'admin-users.html', {'users': users})

# from django.views.generic.edit import CreateView, UpdateView
# from django.urls import reverse_lazy
# from .forms import UserForm
# from django.contrib.auth.models import User
#
# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm
#     success_url = reverse_lazy('user-list')
#
# class UserUpdateView(UpdateView):
#     model = User
#     form_class = UserForm
#     success_url = reverse_lazy('user-list')





    # from django.shortcuts import render
# from django.http import JsonResponse
# import os
# from .models import File
#
# def index(request):
#     if request.method == 'POST':
#         file = request.FILES['file'].read()
#         fileName= request.POST['filename']
#         existingPath = request.POST['existingPath']
#         end = request.POST['end']
#         nextSlice = request.POST['nextSlice']
#
#         if file=="" or fileName=="" or existingPath=="" or end=="" or nextSlice=="":
#             res = JsonResponse({'data':'Invalid Request'})
#             return res
#         else:
#             if existingPath == 'null':
#                 path = 'media/' + fileName
#                 with open(path, 'wb+') as destination:
#                     destination.write(file)
#                 FileFolder = File()
#                 FileFolder.existingPath = fileName
#                 FileFolder.eof = end
#                 FileFolder.name = fileName
#                 FileFolder.save()
#                 if int(end):
#                     res = JsonResponse({'data':'Uploaded Successfully','existingPath': fileName})
#                 else:
#                     res = JsonResponse({'existingPath': fileName})
#                 return res
#
#             else:
#                 path = 'media/' + existingPath
#                 model_id = File.objects.get(existingPath=existingPath)
#                 if model_id.name == fileName:
#                     if not model_id.eof:
#                         with open(path, 'ab+') as destination:
#                             destination.write(file)
#                         if int(end):
#                             model_id.eof = int(end)
#                             model_id.save()
#                             res = JsonResponse({'data':'Uploaded Successfully','existingPath':model_id.existingPath})
#                         else:
#                             res = JsonResponse({'existingPath':model_id.existingPath})
#                         return res
#                     else:
#                         res = JsonResponse({'data':'EOF found. Invalid request'})
#                         return res
#                 else:
#                     res = JsonResponse({'data':'No such file exists in the existingPath'})
#                     return res
#     return render(request, 'upload.html')
# #
# # Create your views here.
# from django.shortcuts import render , redirect
# from django.http import HttpResponse
# from django.contrib.auth.models import User, auth
# from django.contrib import messages
#
#
# # Create your views here.
#
#
#
# def index(request):
#
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username = username, password =password  )
#
#         if user is not None:
#             auth.login(request , user)
#             return redirect('/home')
#         else:
#             messages.info(request, 'invalid username or password')
#             return redirect("/")
#     else:
#         return render(request,'index.html')
#
#
# def register(request):
#
#     if request.method == 'POST':
#
#         email = request.POST['email']
#         username = request.POST['username']
#         password= request.POST['password']
#
#
#         user = User.objects.create_user(username = username , password = password , email = email)
#         user.save()
#         print('user created')
#         return redirect('/custom')
#
#     return render(request,'register.html')
#
#
# def upload_data(request):
#     if request.method='POST':
#         form=DataUploadForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#         else:
#             form=DataUploadForm()
#         uploaded_data=UploadedData.objects.all()
#     return render(request, 'uploaded_data.html',{'form':form,'uploaded_data':uploaded_data})
#
#
# def query_builder(request):
#     return render(request, 'query_builder.html')
