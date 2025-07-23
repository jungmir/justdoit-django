"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from board.views import board_list, board_create, board_delete, board_update
from comment.views import comment_list, comment_create, comment_update, comment_delete

urlpatterns = [
    path("admin/", admin.site.urls),
    # 외부에서 board_list 뷰를 사용할 수 있도록 URL을 추가합니다.
    path("board-list/", board_list, name="board_list"),
    # 외부에서 board_create 뷰를 사용할 수 있도록 URL을 추가합니다.
    path("board-create/", board_create, name="board_create"),
    # 외부에서 board_update 뷰를 사용할 수 있도록 URL을 추가합니다.
    path("board-update/<int:pk>/", board_update, name="board_update"),
    # 외부에서 board_delete 뷰를 사용할 수 있도록 URL을 추가합니다.
    path("board-delete/<int:pk>/", board_delete, name="board_delete"),
    # 외부에서 comment_list 뷰를 사용할 수 있도록 URL을 추가합니다.
    path("comment-list/", comment_list, name="comment_list"),
    # 외부에서 comment_create 뷰를 사용할 수 있도록 URL을 추가합니다.
    path("comment-create/", comment_create, name="comment_create"),
    # 외부에서 comment_update 뷰를 사용할 수 있도록 URL을 추가합니다.
    path("comment-update/<int:pk>/", comment_update, name="comment_update"),
    # 외부에서 comment_delete 뷰를 사용할 수 있도록 URL을 추가합니다.
    path("comment-delete/<int:pk>/", comment_delete, name="comment_delete"),
]
