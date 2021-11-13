from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from .models import Question, Quiz,SaveAns,Answer,Result

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        quiz = Quiz.objects.all()
        for q in quiz:
            if Result.objects.filter(Q(user__id=request.user.id) & Q(quiz__id=q.id)).exists():
                res = Result.objects.get(Q(user__id=request.user.id) & Q(quiz__id=q.id))
                print(q)
        return render(request,'quiz/quiz-list.html',{'quiz':quiz})

def quiz(request,quiz):
    if request.user.is_authenticated:
        quiz = Quiz.objects.get(slug=quiz)
        params = {'quiz':quiz}
        return render(request,'quiz/quiz-page.html',params)
    else:
        return redirect('login')

def saveans(request):
    question = request.POST['queid']
    selopt = request.POST['option']
    quiz = request.POST['quiz']
    qu = Quiz.objects.get(id=quiz)
    q = Question.objects.get(id=int(question))
    correct = Answer.objects.get(Q(questions__id=question) & Q(correct=True))
    if Result.objects.filter(Q(user__id=request.user.id) & Q(quiz__id=quiz)).exists():
        pass
    else:
        if SaveAns.objects.filter(Q(quiz__id=quiz) & Q(question__id=question) & Q(user__id=request.user.id)).exists():
            sa = SaveAns.objects.get(question__id=question)
            sa.selopt = selopt
            sa.save()
        else:
            sa = SaveAns()
            sa.quiz=qu
            sa.user=request.user
            sa.question = q
            sa.selopt = selopt
            sa.correct = correct.id
            sa.save()
        return HttpResponse(correct)

def result(request):
    if request.method=="POST":
        quiz = request.POST['quiz']
        marks = 0
        ans = SaveAns.objects.filter(Q(quiz__id=quiz) & Q(user__id=request.user.id))
        for i in ans:
            if i.selopt == i.correct:
                marks+=10
        if Result.objects.filter(Q(user__id=request.user.id) & Q(quiz__id=quiz)).exists():
            pass
        else:
            res = Result()
            res.user = request.user
            res.quiz = Quiz.objects.get(id=quiz)
            res.marks = marks
            res.save()
        return HttpResponse(marks)