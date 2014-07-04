from django.shortcuts import render, render_to_response, RequestContext


import json

# Create your views here.
def home(request):
     return render(request, "home.html", locals())


def base_line(request):
    '''
    Example of base line chart
    '''

    cat_temp=['cat1','cat2','cat3','cat4','cat5','cat6']
    dat_temp=[1,2,3,4,5,6]

    my_title='My example title'
    series_label='distances'

    my_categories = json.dumps(cat_temp)
    my_data = json.dumps(dat_temp)
    return render_to_response('base_line.html',
                          RequestContext(request,
                                         {'my_categories':my_categories, 'my_data':my_data, 'my_title':my_title,'series_label':series_label,
                                         }))

