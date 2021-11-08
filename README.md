# ✍ 30 Days ✍ 


### 프로젝트 소개
------------
다이어트를 결심하고 작심삼일만에 포기하는 다이어터들을 보며 습관의 필요성을 느껴 프로젝트를 진행했습니다. <br>
계정 생성 후 30일 동안 일지를 기록할 수 있으며 게시판을 통해 사용자들과 의견을 나눌 수 있습니다.

###  주요 기능
------------
* 계정 생성
> Javascript를 이용해 BMI 계산기를 구현 
```
 function BMIcal(){
            var weight = document.getElementById("weight").value;
            var height = document.getElementById("height").value;

            if(weight == 0 || height == 0){
                result = "";
                alert("다시 입력해주세요.");
            }else{
                result = weight/(height*height*0.0001);
                index();
 }
```

>비만, 고도 비만, 초고도비만에 해당하는 사용자만 계정 생성 버튼을 클릭 가능
```
 function index(){
            if(result >= 35){
                document.getElementById("index").innerHTML="초고도비만입니다.";
                joinButton.style.display="block";

            }else if(result >= 30){
                document.getElementById("index").innerHTML="고도비만입니다.";
                joinButton.style.display="block";

            }else if(result >= 25){
                document.getElementById("index").innerHTML="비만입니다.";
                joinButton.style.display="block";

            }else{
                document.getElementById("index").innerHTML="가입조건에 맞지않습니다.";
                joinButton.style.display="none";
  }
 ```
<br>

* 30일 동안의 일지 작성 및 확인
> 계정 생성 당시의 날짜를 기준으로 redirect하는 페이지를 달리 구현

> 계정 생성 30일 이전에는 기록 날짜의 섭취한 칼로리, 운동 종류, 코멘트를 작성 가능

> 계정 생성 30일 이후에는 Chart.js를 이용해 기록한 칼로리 양의 변화를 볼 수 있으며 기록한 일지 확인 가능
```
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
 ```

<br>

* 게시판
> 사용자들은 자유롭게 게시판을 이용할 수 있으며 CRUD 및 페이징, 댓글 기능을 구현

<br>

### 사용 기술
------------
* Web Framework Django
* Python
* Chart.js

### 자료
------------
Django 참고 자료 : 점프 투 장고
><https://wikidocs.net/book/4223> 

### 프로젝트 진행 기간
------------
2021년 3월 ~ 2021년 5월
