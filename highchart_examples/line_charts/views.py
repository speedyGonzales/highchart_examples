from django.shortcuts import render, render_to_response, RequestContext


import json

# Create your views here.
def home(request):
     return render(request, "home.html", locals())


def base_line(request):
    '''
    Example of base line chart
    '''
    des_temp=[1,2,3,4,5,6]
    dis_temp=[1,2,3,4,5,6]

    des = json.dumps(des_temp)
    dis = json.dumps(dis_temp)
    return render_to_response('base_line.html',
                          RequestContext(request,
                                         {'des':des, 'dis':dis, }))

