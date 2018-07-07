from django.shortcuts import render,redirect
from login.models import User,Follow
from .models import Weibo
from review.models import Review
from .forms import writeWeibo,reviewWeibo
def showuser(request,id):
    user = User.objects.get(pk=id)
    if request.GET.get('follow') is not None:
        followid = request.GET.get('follow')
        followuser = User.objects.get(pk=followid)
        try:
            f = Follow.objects.get(user1=user)
            f.user2.add(followuser)
        except:
            f = Follow.objects.create(user1=user)
            f.user2.add(followuser)
            f.save()
    if request.GET.get('cancel') is not None:
        cancelid = request.GET.get('cancel')
        canceluser = User.objects.get(pk=cancelid)

        f = Follow.objects.get(user1=user)
        f.user2.remove(canceluser)
        # except:
        #     f = Follow.objects.create(user1=user)
        #     f.user2.add(followuser)
        #     f.save()


    allUser = User.objects.all()
    try:
        follows = Follow.objects.get(user1=user)
        list_follow = follows.user2.all()
    except:
        list_follow = None


    list_weibo = user.weibo_set.all()

    if request.method=="POST":
        form = writeWeibo(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            w = Weibo(content=content,user=user)
            w.save()
            return render(request, 'weibo/showuser.html', context={'user':user,
                                                                   'list_follow': list_follow,
                                                                   'list_weibo': list_weibo,
                                                                   'form': form,
                                                                   'allUser':allUser})
    else:
        form = writeWeibo()
    return render(request,'weibo/showuser.html',context={'user':user,
                                                         'list_follow':list_follow,
                                                         'list_weibo':list_weibo,
                                                         'form':form,
                                                         'allUser': allUser})

def showweibo(request,id,weiboid):
    iname = request.session["username"]
    iuser = User.objects.get(username=iname)
    iid = iuser.pk
    weibo = Weibo.objects.get(pk=weiboid)
    list_review = weibo.review_set.all()

    if request.method == "POST":
        form = reviewWeibo(request.POST)
        if form.is_valid():
            review = form.cleaned_data['review']
            user = User.objects.get(username=request.session['username'])
            r = Review(review=review,weibo=weibo,user=user)
            r.save()
            return render(request, 'weibo/showweibo.html', context={"weibo": weibo,
                                                                    'list_review': list_review,'form':form,
                                                                    'iid':iid})
    else:
        form = reviewWeibo()
    return render(request,'weibo/showweibo.html',context={"weibo":weibo,
                                                          'list_review':list_review,'form':form,
                                                          'iid':iid})
def showotheruser(request,id):
    iname = request.session["username"]
    iuser = User.objects.get(username=iname)
    iid = iuser.pk
    username = request.session['username']
    meuser = User.objects.get(username=username)
    user = User.objects.get(pk=id)
    try:
        f = Follow.objects.get(user1=meuser)
        f.user2.add(user)
    except:
        f = Follow.objects.create(user1=meuser)
        f.user2.add(user)
        f.save()
    list_weibo = user.weibo_set.all()
    return render(request,"weibo/showotheruser.html",context={"user":user,'list_weibo':list_weibo,
                                                              'iid':iid})



