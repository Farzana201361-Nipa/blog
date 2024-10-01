from django.shortcuts import render
from django.http import HttpResponse




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
def home(request):
    html=""
    for post in posts:
        html += f'''
            <div>
                <h1>{post['id']} - {post['title']}</h1>
                <p> {post['content']}</p>
            
            </div>
        
        '''
    # return HttpResponse("<h1>Hello World!</h1>")
    return HttpResponse(html)

def post(request,id):
    print(type(id))
    return HttpResponse(f"{id}")