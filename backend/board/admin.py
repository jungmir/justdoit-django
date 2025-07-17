from django.contrib import admin

from .models import Board


class BoardCommentInline(admin.StackedInline):
    model = Board.comments.through
    min_num = 0


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "preview", "created_at")
    search_fields = ("title", "content")
    ordering = ("-created_at",)
    inlines = [BoardCommentInline]

    @admin.display(description="내용 미리보기")
    def preview(self, board):
        if len(board.content) > 50:
            return board.content[:50] + "..."
        return board.content
