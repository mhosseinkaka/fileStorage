from django.urls import path
from api.views import addfolder, deletefolder, folderlist, folderitem, addfile, deletefile

urlpatterns = [
    path('add-folder/', addfolder),
    path('delete-folder/<int:folder_id>/', deletefolder),
    path('show-folders/', folderlist),
    path('show-folderitems/<int:folder_id>/', folderitem), 
    path('add-file/<int:folder_id>/', addfile),
    path('delete-file/<int:file_id>/', deletefile)
]