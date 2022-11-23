from django.db import models

# Create your models here.

class AvgPriceByBrand(models.Model):
    brand = models.TextField(primary_key=True, blank=True)
    avg_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avg_price_by_brand'


class AvgPriceByCategory(models.Model):
    category = models.TextField(primary_key=True, blank=True)
    avg_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avg_price_by_category'


class CategoryOccurrence(models.Model):
    word = models.TextField(primary_key=True, blank=True)
    count = models.BigIntegerField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'category_occurrence'

class ExpensiveFurniture(models.Model):
    name = models.TextField(primary_key=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expensive_furniture'

class HasImage(models.Model):
    name = models.TextField(primary_key=True, blank=True)
    image_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'has_image'


class NoNull(models.Model):
    rowid = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'no_null'

    def __str__(self):
    	return self.name

class Output(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    upc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'output'


class OutputTrimmed(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'output_trimmed'


class Target(models.Model):
    rank = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    product_id = models.TextField(blank=True, null=True)
    selected_product_id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    seller = models.TextField(blank=True, null=True)
    review_count = models.TextField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    sale_price = models.TextField(blank=True, null=True)
    regular_price = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    available_in_store = models.TextField(blank=True, null=True)
    available_online = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    is_sponsored = models.TextField(blank=True, null=True)
    product_information = models.TextField(blank=True, null=True)
    image_urls = models.TextField(blank=True, null=True)
    variations = models.TextField(blank=True, null=True)
    product_variants = models.TextField(blank=True, null=True)
    rating_histogram = models.TextField(blank=True, null=True)
    store_id = models.TextField(blank=True, null=True)
    store_location = models.TextField(blank=True, null=True)
    store_telephone = models.TextField(blank=True, null=True)
    store_address = models.TextField(blank=True, null=True)
    search_input = models.TextField(blank=True, null=True)
    search_zipcode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'target'


class Totaloutput(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'totaloutput'
        
class FinaloutputCategories(models.Model):
    name = models.TextField(blank=True, primary_key=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    category1 = models.TextField(blank=True, null=True)
    category2 = models.TextField(blank=True, null=True)
    category3 = models.TextField(blank=True, null=True)
    category4 = models.TextField(blank=True, null=True)
    category5 = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'finaloutput_categories_pkey'
