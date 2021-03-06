from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import DiaryForm
from django.utils import timezone
from .models import Diary


@login_required(login_url='common:login')
def index(request):
    """
    가입한 날로부터 30일 이후인지 확인
    """
    user = request.user
    # 계정을 생성한 날짜 가져오기
    creation = user.date_joined.replace(tzinfo=None)
    # 오늘 날짜 가져오기
    now = datetime.now()
    # 오늘 날짜 - 계정생성일
    # 가입한 날이 1일째이기 때문에 +1을 해준다.
    day = (now-creation).days+1
    if day > 30:
        return redirect('record:after')

    return redirect('record:before')


@login_required(login_url='common:login')
def before(request):
    """
    가입한지 30일 이전의 사용자의 기록 저장
    """
    if request.method == 'POST':
        # 자신이 쓴 글만 가져오기
        diary = Diary.objects.all()
        diary_list = diary.filter(user_id=request.user.id)

        # 오늘 날짜와 비교하여 하루에 한번만 기록할 수 있도록 구현
        for diary in diary_list:
            # 작성일시와 오늘 날짜를 가져옴
            # 현재 datetime
            create = diary.create_date.replace(tzinfo=None)
            now = datetime.now()
            # 문자열로 변환
            create_string = create.strftime('%Y-%m-%d')
            now_string = now.strftime('%Y-%m-%d')
            # 날짜가 같다면 메인페이지로 redirect
            if create_string == now_string:
                return redirect('main:index')

        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.create_date = timezone.now()
            diary.save()
            return redirect('main:index')
    else:
        now = datetime.now()
        joined = request.user.date_joined.replace(tzinfo=None)
        # 가입한 날이 1일째이기 때문에 +1을 해준다.
        date_diff = (now-joined).days+1
        form = DiaryForm()
        context = {'form': form, 'date_diff': date_diff}
        return render(request, 'record/before.html', context)


@login_required(login_url='common:login')
def after(request):
    """
    30일 후 사용자의 모든 기록 확인
    """
    diary = Diary.objects.all()
    diary_list = diary.filter(user_id=request.user.id)
    diary_list_len = len(diary_list)
    calAvg = 0
    timeAvg = 0
    for diary in diary_list:
        calAvg += diary.calorie
        timeAvg += diary.exerciseTime
    calAvg = calAvg/diary_list_len
    timeAvg = timeAvg/diary_list_len
    context = {'diary_list': diary_list, 'calAvg': calAvg, 'timeAvg': timeAvg}
    return render(request, 'record/after.html', context)





