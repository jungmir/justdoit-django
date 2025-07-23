# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Board


def board_list(request):
    """등록된 모든 게시판 정보를 응답하는 View"""

    # 저장된 모든 게시판 정보를 가져옵니다.
    # values 함수를 사용해서 Model 데이터를 Dict 형태로 변환합니다.
    boards = Board.objects.all().values()

    # Dict 형태로 변환된 게시판 정보를 JSON 형태로 응답합니다.
    # created_at 필드는 자동으로 Json으로 변환되지 않아 safe=False 옵션을 사용합니다.
    # safe=False는 리스트 형태의 데이터를 JSON으로 변환할 때 필요합니다.
    return JsonResponse(list(boards), safe=False)


@csrf_exempt
def board_create(request):
    """새로운 게시판을 생성하는 View"""

    # 게시판을 생성하기 위해서 POST 요청을 사용합니다.
    # 요청이 POST가 아닐 경우 에러 응답을 반환합니다.
    if request.method == "POST":
        # 요청에서 게시판 제목과 내용을 가져옵니다.
        title = request.POST.get("title")
        content = request.POST.get("content")

        # 새로운 게시판을 생성합니다.
        board = Board.objects.create(title=title, content=content)

        # 생성된 게시판 정보를 JSON 형태로 응답합니다.
        return JsonResponse(model_to_dict(board))

    # 요청이 POST가 아닐 경우 에러 응답을 반환합니다.
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def board_update(request, pk):
    """게시판 정보를 수정하는 View"""

    # 게시판을 수정하기 위해서 POST 요청을 사용합니다.
    if request.method == "POST":
        try:
            # 게시판을 가져옵니다.
            board = Board.objects.get(pk=pk)

            # 요청에서 수정할 제목과 내용을 가져옵니다.
            title = request.POST.get("title")
            content = request.POST.get("content")

            # 게시판 정보를 수정합니다.
            if title:
                board.title = title
            if content:
                board.content = content
            board.save()

            # 수정된 게시판 정보를 JSON 형태로 응답합니다.
            return JsonResponse(model_to_dict(board))
        except Board.DoesNotExist:
            # 게시판이 존재하지 않을 경우 에러 응답을 반환합니다.
            return JsonResponse({"error": "Board not found"}, status=404)

    # 요청이 PUT가 아닐 경우 에러 응답을 반환합니다.
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def board_delete(request, pk):
    """게시판을 삭제하는 View"""

    # 게시판을 삭제하기 위해서 DELETE 요청을 사용합니다.
    if request.method == "DELETE":
        try:
            # 게시판을 가져와서 삭제합니다.
            board = Board.objects.get(pk=pk)
            board.delete()
            return JsonResponse({"message": "Board deleted successfully"})
        except Board.DoesNotExist:
            # 게시판이 존재하지 않을 경우 에러 응답을 반환합니다.
            return JsonResponse({"error": "Board not found"}, status=404)

    # 요청이 DELETE가 아닐 경우 에러 응답을 반환합니다.
    return JsonResponse({"error": "Invalid request method"}, status=400)
