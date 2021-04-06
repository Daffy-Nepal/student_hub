from django.http import JsonResponse
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
            feedback_id = request.POST.get('feedbackId')
            title = request.POST.get('title')
            description = request.POST.get('description')
            user = request.user
            print(feedback_id)
            if feedback_id == "":
                feedback = Feedback(author=user, title=title,
                                    description=description)
            else:
                feedback = Feedback(id=feedback_id, author=user, title=title,
                                    description=description)
            feedback.save()
            feedback_list = list(Feedback.objects.filter(
                author_id=request.user.id).values())
            return JsonResponse({'feedback_list': feedback_list})
        return JsonResponse({'status': 'Error'})


def delete_feedback(request):
    if request.method == "POST":
        id = request.POST.get('feedback_id')
        feedback = Feedback.objects.get(pk=id)
        feedback.delete()
        return JsonResponse({'status': 'Success'})
    return JsonResponse({'status': 'Error'})


def update_feedback(request):
    if request.method == "POST":
        id = request.POST.get('feedback_id')
        feedback = Feedback.objects.get(pk=id)
        user = request.user.username
        feedback_data = {"id": feedback.id, "author": user,
                         "title": feedback.title, "description": feedback.description}
        return JsonResponse(feedback_data)
