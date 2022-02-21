from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import SingleDomain_DataType_DataUsage_Relative_hover as hover

    
def get(request, **kwargs):
    return render(request, 'index.html', context=None)

def post(request):
    domain = request.POST['domain']
    amount = int(request.POST['corr'])
    corr = hover.plotHeatmap(domain, amount)
    corr = corr.to_dict()
    context_dict = {}
    context_dict['res'] = corr
    context_dict['domain'] = hover.getDomainName()
    context_dict['sampleSize'] = hover.getSampleSize()
    print(hover.getDomainName())
    return render(request, 'resultHover.html', context=context_dict)

def legend(request):
    return render(request, 'legend.html', context=None)