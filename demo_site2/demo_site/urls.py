"""demo_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('contributions/', cont_view, name='cont'),
    path('about/', about_view, name='about'),
    path('query/', query_view, name='query'),
    path('results/', results_view, name='results'),
    path('product/', product_view, name='product'),
    path('analyze/', analyze_view, name='analyze'),
    path('analyze/category_occurrence', analyze_category_occurrence, name='analyze_category_occurrence'),
    path('analyze/avg_price_by_brand', analyze_avg_price_by_brand, name='analyze_avg_price_by_brand'),
    path('analyze/avg_price_by_category', analyze_avg_price_by_category, name='analyze_avg_price_by_category'),
    path('analyze/finaloutputcategories', analyze_finaloutput_categories, name='analyze_finaloutput_categories'),
    path('', home_view),
]
