from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



# Create your views here.
posts =[
    {
        'id': 1,
        'title': 'Chunghua Aluminium',
        'content': 'Chunghua Aluminium is located in Dhaka, Bangladesh. They specialize in the production of high-quality aluminium profiles, used for doors, windows, and various industrial applications. The company is known for its durable and reliable products in the construction sector.'
    },
    {
        'id': 2,
        'title': 'Dhaka Thai Aluminium',
        'content': 'Dhaka Thai Aluminium is one of the leading aluminium companies in Bangladesh, based in Gazipur. They manufacture a wide range of aluminium products including profiles for doors, windows, and curtain walls. The company is a key supplier to both domestic and international markets.'
    },
    {
        'id': 3,
        'title': 'Alco Aluminium',
        'content': 'Alco Aluminium is situated in Chittagong, Bangladesh. Their product line includes aluminium sheets, extrusions, and coils, which are used in the construction, automotive, and packaging industries. Alco is known for its innovative solutions and sustainable practices.'
    },
]
#Home Page

# def home(request):
#     return HttpResponse("Home")
#Access dynamic url using title
def home(request):
    html=""
    for post in posts:
        html += f'''
            <div>
            
            <a href="/post/{post['id']}"> 
                <h1>{post['id']} - {post['title']}</h1></a>
                <p> {post['content']}</p>
            
            </div>
        
        '''
    # return HttpResponse("<h1>Hello World!</h1>")
    # return HttpResponse(html)
    # name = "Farzana"
    # return render(request,'posts/home.html',{"name":name})
    return render(request,'posts/home.html',{'posts': posts})


def post(request,id):
    print(type(id))
    return HttpResponse(f"{id}")

def post(request,id):
    valid_id = False
    for post in posts:
        if post['id'] ==id:
            post_dict = post
            valid_id = True
            break
    if valid_id:   
        html = f'''
            <h1>  {post_dict['title']} </h1>
            <p> {post_dict['content']}</p>
        '''
        return HttpResponse(html)
    else:
        return  HttpResponseNotFound("<h1>Post not Available :)</h1>")
            
#HttpResponseRedirect class to access another url for price
def price(request):
    return HttpResponseRedirect('https://www.banglastall.com/filter/Construction/Thai-Aluminium/ALCO')

def google(request,id):
    #Using reverse function to dynamically generate the urls
    url = reverse("post",args=[id])
    return HttpResponseRedirect(url)
    # return HttpResponseRedirect(f'/posts/{id}/')



