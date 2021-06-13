
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



def index(request):
    """
    question 목록
    """
    # GET 방식 요청 URL에서 page값을 가져올 때 사용한다.
    # (ex) localhost:8000/pybo/?page=1
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    # 페이징처리
    # Paginator 클래스를 사용했으며
    # 페이지당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    question 내용
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    답변 등록 / answer 테이블에 데이터 추가
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        # get 부분이 없어도 실행은 가능
        form = AnswerForm()
        context = {'question':question, 'form':form}
        return render(request, 'pybo/question_detail.html', context)
   

@login_required(login_url='common:login')
def question_create(request):
    """
    질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
        context = {'form': form}
        return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    질문 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    # 현재 사용자와 글을 쓴 사람이 다를 시 다시 해당 게시글로 redirect
    if request.user != question.author:
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        # 화면으로 전달받은 입력값들을 덮어써서 QuestionForm을 생성하라는 의미
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        # instance 매개변수에 question을 지정하면 기존 값을 폼에 채울 수 있음
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    질문 삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    # 현재 사용자와 글을 쓴 사람이 다를 시 다시 해당 게시글로 redirect
    if request.user != question.author:
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')