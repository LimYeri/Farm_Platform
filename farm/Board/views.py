from django.shortcuts import render, redirect,get_object_or_404
from Accounts.models import User
from .models import Board, Comment
from .forms import CommentForm
from django.db.models import Q

# <게시판>
#게시판 전체 리스트
def board(request):
    Boardlist=Board.objects.all().order_by('-id') #게시글 최신순 정렬
    # return render(request, 'Board/board1.html',{'Boardlist':Boardlist})
    return render(request, 'Board/BoardList.html',{'Boardlist':Boardlist})

#게시글 저장
def insert(request):   
    if request.method == 'POST':
        id=request.user
        boardform= Board() #게시글 객체 받아오기
        #입력한 값 POST로 받아오기
        boardform.title = request.POST['title']
        # boardform.date = request.POST['date']
        boardform.content = request.POST['content']
        boardform.user=id #user 객체와 외래키 연결(로그인된 id값->글 작성자로 저장(id))
        boardform.image=request.FILES.get('image')  #사진 받아오기
        boardform.save() #객체에 내용 저장
        # return redirect('detail',boardform.id)#디테일로 리다이렉트
        return redirect('board') #전체 게시판 리스트로 리다이렉트
    return render(request, 'Board/write-post.html')

#게시글 삭제
def detail_delete(request,pk):
    if request.user.is_authenticated:  #로그인된 사용자면
        board= get_object_or_404(Board,pk=pk) #해당 pk값에 맞는 객체 가져오기
        if request.user==board.user:
            board.delete()
    return redirect('board')

#게시글 수정
def detail_edit(request, pk):
    # if request.user.is_authenticated:  #로그인된 사용자면
    board= get_object_or_404(Board,pk=pk) #해당 pk값에 맞는 객체 가져오기
    # if request.user==board.user: #같은 사용자면
    if request.method == "POST":
            board.title = request.POST.get('title')
            board.content = request.POST.get('content')
            board.image=request.FILES.get('image')  #사진 받아오기
            board.save()
            return redirect('board')
    else:
    #내용 수정 전 html 파일에 기존 내용 띄우기 위한 값
            context={ 'title': board.title,
                    'content': board.content,
                    'image': board.image,
              'pk':pk
              }    
            # return render(request, 'Board/Boardedit.html', context)
            return render(request, 'Board/edit-post.html', context)
    

#게시글 상세페이지
def detail(request, pk):
    board= get_object_or_404(Board,pk=pk) #게시판 id값에 해당하는 게시판 상세 객체 받아오기
    comments=Comment.objects.filter(board=pk) #댓글 정렬
    comment_form = CommentForm()
    return render(request, 'Board/view-post.html',{'board':board,'pk':pk,'comment_form':comment_form,'comments':comments})
    # return render(request, 'Board/Boarddetail.html',{'board':board,'pk':pk,'comment_form':comment_form,'comments':comments})


# <댓글>
# 댓글 생성
def comment_create(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            detail = get_object_or_404(Board, pk=pk)
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.board = detail
                comment.user = request.user
                comment.save()
            return redirect('detail', detail.pk)
        # return redirect('login')  #로그인X-> 로그인하러 감(로그인해야 댓글 작성 가능)
 
#댓글 삭제 
def comment_delete(request, board_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('detail', board_pk)  

#게시글 검색
def search(request):
    if request.method == 'POST':
        # 검색어 입력값 저장
        searched = request.POST['searched']
        title_s = Board.objects.filter(Q(title__contains=searched) | Q(content__contains=searched))
        return render(request, 'Board/BoardList.html', {'Boardlist': title_s, 'searched':searched})
    else:
        return redirect('board')
    


