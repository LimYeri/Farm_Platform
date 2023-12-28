# 농촌 소셜/이커머스 (TEAM. 농촌 지지자들👩‍🌾)

**🗓프로젝트 진행 기간:**
2023. 08 ~ 2023. 08 (소요기간: 2주)

**👩🏻‍💻나의 역할:**
    
    [Backend]
    
       -이메일 인증 로그인/로그아웃/비밀번호 변경

       -카카오 소셜 로그인/로그아웃

       -마이페이지

       -농사랑방(농촌 정보공유 게시판) 작성/수정/삭제

       -농사랑방 댓글 작성/삭제

       -농사랑방 게시글 검색

       -회원 채팅 기능 구현


## :bookmark_tabs: 프로젝트 개요
본 프로젝트는 멋쟁이 사자처럼 11기 중앙 해커톤 TEAM. 농촌 지지자들👩‍🌾로 부터 시작되었으며, 농촌의 정보 격차를 해소하기 위해 농민들을 타깃으로 한 정보 공유 종합 소셜미디어 서비스이다. 농산물 마켓 및 일손 구하기 기능을 통한 농촌🌾과 도시🏬를 연결한다.
<br><br>
 📌 농촌은 도시에게 단기 일자리, 봉사활동 시간, 유기농 농작물등을 제공한다.<br><br>
 📌 도시는 농촌에게 일손을 제공하고, 농촌의 경제 성장(농작물 구매)을 돕는다.<br><br>
 📌 농민과 농민은 농사 정보를 주고 받는다.(커뮤니티의 기능)<br><br>
       
## :bookmark_tabs: 프로젝트 설명
**Target: 이런 사람에게 추천해요** 🎯<br>
 📌 내가 직접 재배한 농산물을 소량 판매하고 싶어요!<br>
 📌 소규모 일손을 구하고 싶어요! <br>
 📌 언제 비료를 줘야 하나요? 도와줘요 농사 고수님들~<br>
 📌 봉사 시간이 필요해요!<br>
<br>

**About 농촌 소셜/이커머스** ❗️  <br>
 ✔️ **최신 농업 기술 모음집:** 전문가가 알려주는 최신 농업 기술 정보<br>
 ✔️ **영농 일지:** 회원별 농사 일지  <br>
 ✔️ **기상 정보 제공:** 실행 위치(지역)에 따른 온도, 강수확률, 일몰, 일출시간 등 농사에 필요한 정보 제공  <br>
 ✔️ **농사랑 방:** 농사 정보 공유 자유게시판 <br>
 ✔️ **일손 구하기:** 일손 구인 게시판, 소규모/단기 농촌 봉사활동  <br>
 ✔️ **농산물 마켓:** 농부가 재배부터 판매까지 믿고 사는 농산물  <br>
 ✔️ **농약 정보:** 농약 추천부터 사용방법까지 농약에 대한 모든 것 <br><br>
 <div align="center">
<img width="707" alt="스크린샷 2023-12-29 오전 2 33 11" src="https://github.com/kjw4420/Farm_Platform/assets/97749184/9389748b-ae12-4712-a309-8284586830a4"><br>
     <img width="707" alt="스크린샷 2023-12-29 오전 2 33 21" src="https://github.com/kjw4420/Farm_Platform/assets/97749184/9c8eb038-6fd2-4af9-b58a-c8c36a797193"><br>
<img width="707" alt="스크린샷 2023-12-29 오전 2 33 28" src="https://github.com/kjw4420/Farm_Platform/assets/97749184/eec54bd3-cf5d-4a76-a5c7-3ab1aee633f8">
 </div>






## :bookmark_tabs: 기능 소개
 ✔️**회원가입 및 로그인:**<br>
-이메일 인증 회원가입/로그인 및 소셜(카카오) 회원가입/로그인을 지원한다. <br><br>
 ✔️**게시글 CRUD/댓글:**<br>
-각종 농촌 정보, 농산물 판매 게시글, 농촌 봉사활동 구인 게시글 등의 CRUD 구현. 자유 게시판 형태의 농사랑 방은 게시글에 댓글을 작성/삭제하는 기능을 추가하여 정보 공유의 목적을 뚜렷하게 한다.<br><br>
 ✔️**채팅:**<br>
-개인 간의 거래(농산물 거래, 농촌 봉사활동 신청)을 위해 게시글 pk 값으로 채팅방을 개설하여 사용자가 대화할 수 있도록 한다.(채팅을 통한 사용자 간 거래)<br><br>
 ✔️**검색:**<br>
-게시판에서 키워드, 제목 등의 검색을 지원한다.<br><br>
 ✔️**좋아요(스크랩):**<br>
-관리자만 게시글을 작성할 수 있는 최신 농업 기술 모음집과 거래 목적의 게시판(농산물 거래, 일손 구하기)은 좋아요 기능을 구현하여 따로 확인할 수 있도록 한다.<br><br>
 ✔️**마이페이지:**<br>
-회원별 활동 파악. 회원 정보, 로그아웃 및 내가 찜한 상품, 내가 찜한 봉사, 나의 농사랑 방으로 자신이 스크랩한 글과 작성한 게시판 글을 관리한다.<br><br>

## :bookmark_tabs: 문제해결: 채팅 기능 개선
처음 장고 Channels로 채팅 기능을 만들었을 때는 사용자가 채팅방에서 나누는 대화가 행 바꿈으로만 구별되어 누구와 대화를 나누고 있는지 알 수 없었습니다. 또 두 사람이 겹쳐서 같은 말을 했을 때 누가 한 말인지도 구분하기 어려웠습니다. 이 문제를 해결하기 위해서는 사용자 아이디 노출 기능이 필요하다고 생각했습니다.
 <div align="center">
<img width="1358" alt="스크린샷 2023-12-07 오전 2 58 33" src="https://github.com/kjw4420/Farm_Platform/assets/97749184/6740cadc-09b8-42c0-9c26-04ca57b7013a">
개선이 필요한  Chatting 창
</div>
고민 끝에, 채팅방 html에서 <input type="text" id="username" value="{{user.first_name}}" />으로 현재 로그인된  user의 이름을 받고 js와   consumers.py를 통해 Sender(==user.first_name)을 전달하도록 코드를 변경했습니다. 

- consumers.py:  모든 요청을 받아들이는 비동기적인 WebSocket 소비자 역할을 하게 된다. 즉 메시지를 클라이언트로부터 받아서 그대로 클라이언트에게 전달하는 기능을 함.

```python
function sendMessage() {
        var sender = document.getElementById("username").value;
        var message = document.getElementById("message").value;

        chatSocket.send(
          JSON.stringify({
            message: message,
            sender: sender,
          })
        );

        document.getElementById("message").value = "";
      }
```
 <div align="center">
chat.html/js
     </div>
     
```python
async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
      
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender':sender  #이거 추가 사항
            }
        )
        

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender=event['sender']
    

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender':sender,  #이거 추가 사항
        }))
```
 <div align="center">
        chat/consumers.py
 </div>

## :bookmark_tabs: Chat
농산물 거래/ 봉사활동 신청 시 채팅 사용   <br>
 <div align="center">
<img width="512" alt="스크린샷 2023-12-29 오전 2 44 13" src="https://github.com/kjw4420/Farm_Platform/assets/97749184/59ed4c47-c01e-49f4-98b7-4a101c1d9e74">
 </div>
      - 같은 게시글에서 채팅창 버튼 클릭시 동일한 채팅방으로 이동(pk값: 게시글 pk값)
    
    채팅 내용 전송 시, 내용 작성자 닉네임(user. first_name)도 함께 전송  
    
        **카카오 로그인은 전체 사용자명이 first_name으로 들어감
    
<div align="center">
<img width="719" alt="스크린샷 2023-12-29 오전 2 44 50" src="https://github.com/kjw4420/Farm_Platform/assets/97749184/98815d33-9c0d-4a89-b681-a78f9b7e8598">
 </div>
     - Django Channels, WebSocket, ASGI/Daphne Server: 채팅 통신 <br>


 <div align="center">
<img width="584" alt="스크린샷 2023-12-29 오전 2 45 30" src="https://github.com/kjw4420/Farm_Platform/assets/97749184/f10acbf9-a214-42af-a1b9-527c50f45de9"><br>통신</div> 
<br>
      - Docker위에 Redis 설치: 채팅 데이터 관리 

## 👩🏻‍💻 멤버


### Front-end

|               | github                             |
| ------------- | ---------------------------------- |
| 김다빈 |    https://github.com/KIMDAB1N|
| 심규민      |   https://github.com/gyumin6349      |


### back-end

|               | github                             |
| ------------- | ---------------------------------- |
| 김지원  |https://github.com/kjw4420    |
| 임예리        |  https://github.com/LimYeri       |
| 조서현      |   https://github.com/westnowise      |

### 디자인

김다빈

## :hammer_and_wrench: 사용 기술

### Front-end

**프로그래밍 언어**<br>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=white"/>
<br>


### Back-end

**언어**<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
 <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=white"/><br><br>
**프레임워크/라이브러리**<br>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/> <br>

**데이터베이스**<br>
<img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=Sqlite&logoColor=white">

**배포**<br>
<img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=aws&logoColor=white">

