from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import *
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
import json
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage








                    # Home Page

def index(request):


    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')

    try:
        posts= paginator.page(page)
        
    
    except PageNotAnInteger:
        posts= paginator.page(1)

    except EmptyPage:
         posts= paginator.page(paginator.num_pages)


    
    total_posts = Post.objects.count() 



 

    context = {'posts':posts, 'categories':categories, 'paginator':paginator, 'total_posts': total_posts}
    return render (request, 'index.html', context)




            # DetailView

def blog_body(request, slug):
    category= request.GET.get('category')
    if category ==  None:
        posts = Post.objects.filter()




    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id).order_by('-date_created')[:6]

    comments = Comment.objects.filter(blog=post)
    form = CommentForm()
    msg = False

    if request.user.is_authenticated:
         user = request.user



    # if post.likes.filter(id=user.id).exists():
    #      msg = True

    



    if request.method=='POST':

        if request.user.is_authenticated:
            user = request.user

            # if post.likes.filter(id=user.id).exists():
            #     post.likes.remove(user)
            #     msg = False

            # else:
            #     post.likes.add(user)
            #     msg = True


            
            
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.user = request.user
            comment.save()
            return redirect ('detail', slug=post.slug)


    categories = Category.objects.all()
    
    context = {

               'post': post, 
               'posts':posts, 
               'categories':categories,
               'form':form, 'comments':comments, 
               'msg':msg

              }
    

    return render (request, 'blog_detail.html', context)




# def like_post(request):

#     data = json.loads(request.body)
#     id = data['id']
#     post = Post.objects.get(id=id)

#     if request.user.is_authenticated:
#         post.likes.add(request.user)



#     return JsonResponse('It is working', safe=False)








   





# def create_post(request):
#     form = PostBlog

#     if request.method == 'POST':
#         form = PostBlog(request.POST, request.FILES)
#         if form.is_valid():
#             post= form.save(commit=False)
#             post.slug = slugify(post.title)
#             post.save()
            
#             return redirect ('index')
#         context = {'form':form}
#         return render (request, 'create_post.html', context)



                # Blog CreateView

def create_post(request):
    profile = request.user.userprofile
    
    
    
    if request.method == 'POST':
        
        form = PostBlog(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.author = profile
            messages.info(request, 'Your blog has been posted successfully.')
            post.save()
            return redirect('index')
        else:
            messages.error(request, 'Failed to post your blog. Try again.')    
    else:
        form = PostBlog()
        categories = Category.objects.all()
        posts = Post.objects.all().order_by('-date_created')
    context = {'form': form, 'categories':categories, 'posts':posts}
    return render(request, 'create_post.html', context)


            # UpdateView

@login_required
def update_post(request, slug):
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    post = Post.objects.get(slug=slug)
    form = PostBlog(instance=post)
    if request.method == 'POST':
        form=PostBlog(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Blog updated successfully.')
            return redirect ('detail', slug=post.slug)
        
    context ={'form':form, 'categories':categories, 'posts':posts}
    return render (request, 'update_post.html', context)



                # DeleteView

@login_required
def delete_post(request, slug):
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    post = Post.objects.get(slug=slug)
    form = PostBlog(instance=post)
    if request.method == 'POST':
        post.delete()
        messages.warning(request, 'You deleted a blog.')
        return redirect ('index')

    context = {'form':form, 'categories':categories, 'posts':posts}
    return render (request, 'delete_post.html', context)






# def test (request):
#     return render (request, 'test.html')







# def category_page(request,pk):

# #     category = Category.objects.get(category_id=pk)
# #     posts = Post.objects.filter(category=category)
# #     context = {'category':category, 'posts':posts}
# #     return render (request, 'categorypage.html', context)
   
#     try:
#         category = Category.objects.get(category_id=pk)
#         post = Post.objects.filter(category=category)
#         return render (request, 'categorypage.html', {'post':post, 'category':category})


#     except:
#         messages.info(request, 'No results found')
#         return redirect('index')





# def  category_page(request):
#     categories = Category.objects.all()
#     # cats = Category.objects.get(category_id=pk)
#     context = {'categories':categories}
#     return render (request, 'categorypage.html', context)





                    # Category

def category_page(request, pk):
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    category = get_object_or_404(Category, category_id=pk)
    posts = Post.objects.filter(category=category)
      

    context = {'category': category, 'posts': posts, 'categories':categories, 'posts':posts}
    return render (request, 'categorypage.html', context)




                # Search Section

def search_bar (request):
    posts = Post.objects.all().order_by('-date_created')
    categories = Category.objects.all()
    queryset = ''
    queryset1 = ''


    context = {
        'queryset':queryset,
        'queryset1': queryset1,
        
    }

    if request.method == 'GET':
        queryset = request.GET.get('search')
        queryset1 =  Post.objects.filter(title__icontains=queryset)
    
    

        context = {
            'queryset':queryset,
            'queryset1': queryset1,
            'categories':categories,
            'posts':posts
        }
   
    


    return render (request, 'search_bar.html', context)





# def contact(request):

#     categories = Category.objects.all()
#     posts = Post.objects.all().order_by('-date_created')

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             send_mail(
#                 f"Contact Form Submission from {name}",
#                 subject,
#                 message,
#                 email,  # From email
#                 [settings.EMAIL_HOST_USER],  # To email
#             )
#             messages.info(request, "Thank you for contacting us, we'll get back to you soon.")
#             return redirect ('contact')
#     else:
#         form = ContactForm()
   

#     context = {'categories':categories, 'posts':posts, 'form':form}


#     return render (request, 'contact.html', context)







        # Contact Form

def contact(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-date_created')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        myquery= Contact(name=name, email=email, subject=subject, message=message)
        myquery.save()
        messages.info(request, 'Your message has been delivered. We will get back to you soon.')
        return redirect ('contact')
        

  
   
    context = {'categories': categories, 'posts': posts}
    return render(request, 'contact.html', context)






                # About


def about (request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-date_created')


    context = {'categories': categories, 'posts': posts}


    return render (request, 'about.html', context)



