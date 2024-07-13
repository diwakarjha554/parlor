from django.shortcuts import render

def Login(request):
    context = {
        "title": 'Admin Login'
    }
    return render(request,"server/Admin_Login.html" , context=context)






def Data(request):
    context = {
        'title': 'Data View'
    }
    return render(request,'server/DataBase.html' , context=context)




def Category(request):
    context = {
        'title' : 'Category Edits'
    }
    return render(request,'server/Category.html' , context=context)





def Product(request):
    context = {
        'title' : 'Products Edit'
    }
    return render(request, 'server/Product.html' , context = context)





def Service(request):
    context = {
        'title' : "Services Edit"
    }
    return render(request,'server/Service.html' , context=context)