from django.shortcuts import render
from django.http import HttpResponse
from .models import NoNull, CategoryOccurrence, AvgPriceByBrand, AvgPriceByCategory, FinaloutputCategories
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
def home_view(request, *args, **kwargs):
    searchterm = None
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})
	
def cont_view(request, *args, **kwargs):
    return render(request, "contributions.html", {})
	
def query_view(request, *args, **kwargs):
    if request.POST.get('searchQueryInput'):
        request.session['search_term'] = str(request.POST.get('searchQueryInput'))
        request.session["sort_type"] = "reset"
    if request.POST.get('sort'):
        request.session["sort_type"] = str(request.POST.get('sort'))
    return render(request, "query.html", {})
	
@xframe_options_exempt
def results_view(request):
    searchterm = request.session.get('search_term')
    sortterm = request.session.get('sort_type')
    if sortterm == "Ascending price":
        query_list = NoNull.objects.filter(name__contains=searchterm).order_by('price') | NoNull.objects.filter(description__contains=searchterm).order_by('price')
    elif sortterm == "Descending price":
        query_list = NoNull.objects.filter(name__contains=searchterm).order_by('-price') | NoNull.objects.filter(description__contains=searchterm).order_by('-price')
    elif sortterm == "Alphabetical":
        query_list = NoNull.objects.filter(name__contains=searchterm).order_by('name') | NoNull.objects.filter(description__contains=searchterm).order_by('name')
    else:
        query_list = NoNull.objects.filter(name__contains=searchterm) | NoNull.objects.filter(description__contains=searchterm)
    return render(request, "results.html", {'query_list' : query_list})

def product_view(request, *args, **kwargs):
	product = NoNull.objects.filter(rowid=request.GET.get("id"))
	return render(request, "product.html", {"product": product})

def analyze_view(request, *args, **kwargs):
	return render(request, "analyze.html", {})

def analyze_category_occurrence(request, *args, **kwargs):
	categories = CategoryOccurrence.objects.order_by("-count")
	return render(request, "analyze_category_occurrence.html", {"categories": categories})

def analyze_avg_price_by_brand(request, *args, **kwargs):
	brands = AvgPriceByBrand.objects.order_by("-avg_price")
	return render(request, "analyze_avg_price_by_brand.html", {"brands": brands})

def analyze_avg_price_by_category(request, *args, **kwargs):
	categories = AvgPriceByCategory.objects.order_by("avg_price")
	return render(request, "analyze_avg_price_by_category.html", {"categories": categories})

def analyze_finaloutput_categories(request, *args, **kwargs):
    cat=request.GET.get("cat")
    if request.POST.get('searchQueryInput'):
        cat2= str(request.POST.get('search_term'))
    
    if(cat):
        query_str = "SELECT * " + "FROM finaloutput_categories_pkey" +" WHERE category1 LIKE \"%"+cat+"%\" "+" OR category2 LIKE \"%"+cat+"%\" "+" LIMIT 1000;"
        categories = FinaloutputCategories.objects.raw(query_str)
    else:
        categories = FinaloutputCategories.objects.raw("SELECT * FROM finaloutput_categories_pkey LIMIT 1000;")
    
    return render(request, "analyze_finaloutputcategories.html", {"categories": categories})

