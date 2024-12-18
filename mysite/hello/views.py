from django.http import HttpResponse

# Create your views here.

def myview(request) :
    if not request.session.session_key:
        request.session.create()
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['nsum_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '57fc6f44', max_age=1000)
    return resp