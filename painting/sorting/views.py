from django.shortcuts import render, redirect, get_object_or_404
from .models import Sorting, Shop, Feedbackall
from .forms import ShopForm, FeedbackallForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# только для зарегистрированных пользователей.
from django.contrib.auth.decorators import login_required





# @login_required(login_url='index') # -------------!!!!
def about(request):
    return render(request, 'sorting/about.html')


# - Show page with pictures
def index(request):
    projects = Sorting.objects.all()
    return render(request, 'sorting/index.html', {'projects': projects})






                                       #  SHOP
def shop(request):
    pictures = Shop.objects.exclude(genre='sold')
    context = {'pictures': pictures}
    return render(request, 'sorting/shop.html', context)







def placing(request):
    form = ShopForm()
    if request.method == 'POST':
        form =ShopForm(request.POST, request.FILES)
        if  form.is_valid():
            form.save()
            return redirect('shop')
    context = {'form': form}
    return render(request, 'sorting/placing.html', context)



# ----------------- CURRENT --------------

def picture(request, picture_pk):
    picture = get_object_or_404(Shop, pk=picture_pk)
    if request.method == "GET":

        form  = ShopForm(instance = picture)
        return render(request, 'sorting/picture.html', {'picture': picture, 'form':form})

    else:
        try:
            form = ShopForm(request.POST, instance = picture)
            form.save()
            return redirect('shop')
        except ValueError:
            return render(request, 'sorting/shop.html',
                          {'picture': picture, 'form': form, 'error': 'Неверные данные'})





def soldpicture(request, picture_pk):
    picture = get_object_or_404(Shop, pk=picture_pk)
    if request.method == 'POST':
        picture.genre='sold'
        picture.save()
        return redirect('completedsold')





@login_required(login_url='loginuser')
def deletepicture (request, picture_pk):
    picture = get_object_or_404(Shop, pk=picture_pk )
    if request.method == 'POST':
        picture.delete()
        return redirect('shop')


def completedsold(request):
    teams = Shop.objects.filter(genre='sold')
    return render(request, 'sorting/completedsold.html', {'teams': teams})









# @login_required
# def deleteteam(request, team_pk):
#     team = get_object_or_404(Team, pk=team_pk, user=request.user)
#     if request.method == 'POST':
#         team.delete()
#         return redirect('shop')






                        #           F E E D B A C K


@login_required(login_url='loginuser') # redirection
def feedback(request):
    form = FeedbackallForm()
    # return render(request, 'sorting/feedback.html')

    if request.method == 'POST':
        form =FeedbackallForm(request.POST, request.FILES)
        if  form.is_valid():
            form.save()
            return redirect('feedbackall')
    context = {'form': form}
    return render(request, 'sorting/feedback.html', context)




def feedbackall(request):
    feedbacks = Feedbackall.objects.all()
    context = {'feedbacks': feedbacks}
    return render(request, 'sorting/feedbackall.html', context)












