from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from .models import Review
from users.models import User
from .forms import ReviewForm

# Create your views here.
class ReviewView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'comments/reviews.html'
    extra_context = {'title': 'Отзывы'}
    paginate_by = 8

    def get_queryset(self):
        order_by = self.request.GET.get('order_by')
        if order_by:
            reviews = super().get_queryset().order_by(order_by)
        else:
            reviews = super().get_queryset().order_by('-time_create')
        return reviews


class CreateReviewView(LoginRequiredMixin, CreateView):
    form_class = ReviewForm
    template_name = 'comments/create_review.html'
    success_url = reverse_lazy('review:reviews')
    extra_context = {'title': 'Отзыв'}

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial