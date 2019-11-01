from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import *
from django.db.models import Q

# Create your views here.
class Home(ListView):
    model = YoutuberModel
    template_name = 'congtube/home.html'
    context_object_name = 'home_object'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('c')
        if query:
            youtuber_list = YoutuberModel.objects.filter(name__icontains=query)
        elif category:
            category_list = YoutuberCategoryModel.objects.filter(category_id=category)
            youtuber_list = []
            for youtuber in category_list:
                youtuber_list.append(YoutuberModel.objects.get(id=youtuber.youtuber_id))
        else:
            youtuber_list = YoutuberModel.objects.all()
        models = {
            'youtuber_list': youtuber_list,
            'category_list': CategoryModel.objects.all()
        }
        return models

class Detail(DetailView):
    model = YoutuberModel
    template_name = 'congtube/youtuber_detail.html'
    context_object_name = 'object'

    def get_object(self):
        youtuber_id = self.kwargs['pk']
        youtuber = YoutuberModel.objects.get(id=youtuber_id)
        category = YoutuberCategoryModel.objects.filter(youtuber_id=youtuber_id)

        category_list=[]
        for each in category:
            category_list.append(CategoryModel.objects.get(id=each.category_id))

        subscriber_count = len(SubscriberModel.objects.filter(youtuber_id=youtuber_id))
        review = ReviewModel.objects.filter(youtuber_id=youtuber_id)
        recommendation_youtuber = YoutuberModel.objects.filter(~Q(id=youtuber_id))
        youtuber.views += 1

        youtuber.save()

        models = {
            'youtuber': youtuber,
            'category': category_list,
            'review': review,
            'recommendation_youtuber': recommendation_youtuber,
            'subscriber_count': subscriber_count
        }

        return models

def add_review(request, pk):
    review = ReviewModel()
    review.youtuber_id = pk
    review.user_id = 1
    review.review_text = request.POST['review']
    review.register_date = timezone.now()

    review.save()
    return HttpResponseRedirect('/')

def add_subscriber(request, pk):
    subscriber = SubscriberModel()
    subscriber.youtuber_id = pk
    subscriber.user_id = 1
    subscriber.register_date = timezone.now()

    subscriber.save()

    return HttpResponseRedirect('/detail/' + str(pk))

