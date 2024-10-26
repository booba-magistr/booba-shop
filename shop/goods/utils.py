import keyword
from goods.models import Product
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(queryset):
    vector = SearchVector("name", "description")
    query = SearchQuery(queryset)
    return (
        Product.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
