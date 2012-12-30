# Create your views here.
from django.shortcuts import render_to_response
from news.article.models import List

def news_report(request):
  article_listing = []
  for article_list in List.objects.all():
    article_dict = {}
    article_dict['news_object'] = article_list
    article_dict['item_count'] = article_list.item_set.count()
    article_dict['items_title'] = article_list.title
    article_dict['items_complete'] = article_list.item_set.filter(completed=True).count()
    article_dict['percent_complete'] = int(float(article_dict['items_complete'])/article_dict['item_count']*100)
    article_listing.append(article_dict)
  return render_to_response('news_report.html',{'article_listing':article_listing})


