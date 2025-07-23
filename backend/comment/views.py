# Create your views here.
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Comment


def comment_list(request):
    """등록된 모든 댓글 정보를 응답하는 View"""

    # 저장된 모든 댓글 정보를 가져옵니다.
    # values 함수를 사용해서 Model 데이터를 Dict 형태로 변환합니다.
    comments = Comment.objects.all().values()

    # Dict 형태로 변환된 댓글 정보를 JSON 형태로 응답합니다.
    # safe=False는 리스트 형태의 데이터를 JSON으로 변환할 때 필요합니다.
    return JsonResponse(list(comments), safe=False)


@csrf_exempt
def comment_create(request):
    """새로운 댓글을 생성하는 View"""

    # 댓글을 생성하기 위해서 POST 요청을 사용합니다.
    if request.method == "POST":
        # 요청에서 댓글 내용을 가져옵니다.
        content = request.POST.get("content")

        # 새로운 댓글을 생성합니다.
        comment = Comment.objects.create(content=content)

        # 생성된 댓글 정보를 JSON 형태로 응답합니다.
        return JsonResponse(model_to_dict(comment))

    # 요청이 POST가 아닐 경우 에러 응답을 반환합니다.
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def comment_update(request, pk):
    """댓글 정보를 수정하는 View"""

    # 댓글을 수정하기 위해서 POST 요청을 사용합니다.
    if request.method == "POST":
        try:
            # 댓글을 가져옵니다.
            comment = Comment.objects.get(pk=pk)

            # 요청에서 수정할 내용을 가져옵니다.
            content = request.POST.get("content")

            # 댓글 정보를 수정합니다.
            if content:
                comment.content = content
            comment.save()

            # 수정된 댓글 정보를 JSON 형태로 응답합니다.
            return JsonResponse(model_to_dict(comment))
        except comment.DoesNotExist:
            # 댓글이 존재하지 않을 경우 에러 응답을 반환합니다.
            return JsonResponse({"error": "comment not found"}, status=404)

    # 요청이 PUT가 아닐 경우 에러 응답을 반환합니다.
    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def comment_delete(request, pk):
    """댓글을 삭제하는 View"""

    # 댓글을 삭제하기 위해서 DELETE 요청을 사용합니다.
    if request.method == "DELETE":
        try:
            # 댓글을 가져와서 삭제합니다.
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return JsonResponse({"message": "comment deleted successfully"})
        except comment.DoesNotExist:
            # 댓글이 존재하지 않을 경우 에러 응답을 반환합니다.
            return JsonResponse({"error": "comment not found"}, status=404)

    # 요청이 DELETE가 아닐 경우 에러 응답을 반환합니다.
    return JsonResponse({"error": "Invalid request method"}, status=400)
