from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "preview", "created_at")
    search_fields = ("content",)
    ordering = ("-created_at",)

    @admin.display(description="내용 미리보기")
    def preview(self, comment):
        if len(comment.content) > 50:
            return comment.content[:50] + "..."
        return comment.content
