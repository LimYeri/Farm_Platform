# chat/views.py
from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from Board.models import Board

def index(request):
    # return render(request, 'chat/index.html', {})
     board= get_object_or_404(Board,pk=11) #해당 pk값에 맞는 객체 가져오기
     return render(request, 'chat/btn_test.html',{'board':board})

def room(request, room_name):
    return render(request, 'chat/room1.html', {
        'room_name': room_name,
    })
    
    
def DABINroom(request, room_name):
    return render(request, 'chat/chat-dabin.html', {
        'room_name': room_name,
    })    
#글 작성자==로그인된 사용자 채팅방 만들기


#방 만들기: 버튼 누르면 방 제목 전송

#action="{% url 'room' 'Hello' %}"