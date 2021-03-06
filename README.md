### Purpose

인공지능 교육 사이트, [publicai-edu](https://publicai-edu.com/)에서 제공되는 퀴즈와 과제들을 풀기 위해 존재하는 Tool Package입니다. 
주요 기능으로는 1) 문제를 풀고 서버로 제출하는 기능과, 2) 문제를 풀기 위해 필요한 데이터셋을 다운로드 받는 기능으로 구성되어 있습니다.

해당 코드들은 Open Source로 공개되어 있지만, 해당 툴의 기능을 이용하기 위해서는 Public-ai EDU에서 강의를 등록한 후 풀기 위해 필요한 노트북을 제공받아야 합니다. 


### Installation

pip를 이용해 간단히 설치할 수 있습니다. 환경이 안정화된 후, 추후 pypi에도 게재할 예정입니다.


````shell
pip install git+https://github.com/public-ai/publicai-learntools.git
````


### Usage

수업에서 제공하는 퀴즈는 기본적으로 주피터 노트북의 형태로 구성되어 있습니다.    

#### 1. 로그인하기 

제일 첫 Cell은 로그인 Cell입니다. 수업에서 발급받은 ID와 Password로 가입해주시면 됩니다. 

#### 2. 문제 풀기

문제를 읽은 후, 작성할 답을 제출란에 지정되어 있는 변수에 할당하면 됩니다.
 

#### 3. 문제 제출하기

문제를 제출할 때에는 작성한 소스코드도 함께 서버로 전달됩니다. 이를 바탕으로 수업에서는 코드 리뷰의 형식으로 수업을 진행합니다. 


