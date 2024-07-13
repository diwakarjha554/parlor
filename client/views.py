from django.shortcuts import render






def index(request):

    context = {
        'title': 'Advance beauty'
    }

    return render(request, 'Client/base.html', context=context)






def About_Us(request):

    context = {
        'title': 'About Advanced Beauty'
    }
    return render(request, 'Client/About.html' , context=context)





def Categories(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Categories.html' , context=context)





def Client_Login(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Client_Login.html' , context=context)





def Contact(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Contact.html' , context=context)





def Cart(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Cart.html' , context=context)






def Service(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Service.html' , context=context)







def Shop(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Shop.html' , context=context)








def Check_Out(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Checkout.html' , context=context)







def Items(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Item.html' , context=context)







def Confirm(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Thank-you.html' , context=context)





def Review(request):

    context = {
        'title': 'Advanced Beauty'
    }
    return render(request, 'Client/Review.html' , context=context)