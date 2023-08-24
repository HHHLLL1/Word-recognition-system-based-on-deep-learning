from ocr import views
from django.urls import path

app_name = 'Django_OCR_backend.ocr'

urlpatterns = [
    path('upload/', views.Upload.as_view(), name='upload'),
    path('uploadlan/', views.Upload_lan.as_view(), name='uploadlan'),
    path('uploadidcard/', views.Upload_idcard.as_view(), name='uploadidcard'),
    path('uploadcarcard/', views.Upload_carcard.as_view(), name='uploadcarcard'),
    path('history/', views.Historydata.as_view(), name='history'),
    # path('', PostList.as_view(), name='listpost'),
    # path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    # path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    # # Post Admin URLs
    # path('admin/create/', CreatePost.as_view(), name='createpost'),
    # path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    # path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    # path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]
