from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Vote
from django.contrib.auth.models import User
from django.utils import timezone


def home(request):
    products = Product.objects


    return render(request, 'products/home.html',{'products':products})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            vote = Vote()

            vote.user = request.user
            vote.save()
            product.save()
            product.votes_total.add(vote)
            product.save()

            product.votes_total_int =  product.votes_total.all().count()
            product.save()
            print("count for product", product.votes_total_int)

            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    print("here is the total vote count:", product.votes_total_int)
    return render(request, 'products/detail.html',{'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        votes = product.votes_total.all()
        currentUser = request.user
        flag = False
        #aUser = product.
        for vote in votes:
            if vote.user == currentUser:
                vote.delete()
                flag = True

        if flag == False:
            vote = Vote()
            vote.user = request.user
            vote.save()
            product.votes_total.add(vote)
            product.save()
        product.votes_total_int =  product.votes_total.all().count()
            #product.votes_total.all().remove(currentUser)
        #return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})


        #product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
