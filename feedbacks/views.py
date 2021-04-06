from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import FeedBackForm
from .models import Feedback

# Create your views here.


def feedbacks(request):
    form = FeedBackForm
    feedbacks = Feedback.objects.filter(author_id=request.user.id)
    context = {
        'form': form,
        'feedbacks': feedbacks
    }
    return render(request, 'feedbacks/feedback.html', context)


def create_feedback(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            user = request.user
            feedback = Feedback(author=user, title=title,
                                description=description)
            feedback.save()
            feedback_list = list(Feedback.objects.filter(
                author_id=request.user.id).values())
            return JsonResponse({'feedback_list': feedback_list})
        return JsonResponse({'status': 'Error'})
