from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Folder, File
import json

# Create your views here.
@csrf_exempt
def addfolder(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Folder.objects.create(
            name = data.get('name') 
        )
        return HttpResponse(f"folder added! id : {Folder.objects.latest('id').id}")
    
@csrf_exempt
def deletefolder(request, folder_id):
    if request.method == "DELETE":
        Folder.objects.get(id=folder_id).delete()
        return HttpResponse("Folder Deleted!")
    
@csrf_exempt
def folderlist(request):
    item = Folder.objects.all().order_by("name").values('id', 'name')
    item2 = list(item)
    return JsonResponse(item2, safe=False)

@csrf_exempt
def addfile(request, folder_id):
    folder = Folder.objects.get(id=folder_id)
    if request.method == 'POST':
        files_item = request.FILES.getlist('files')
        uploaded_files = []
        for file in files_item:
            file = File.objects.create(
                folder = folder,
                file = file,
                name = file.name
            )
            uploaded_files.append({
                'id': file.id,
                'name': file.name,
                'created_at': file.created_at,
                'file': file.file.url
            })
        return HttpResponse("files added!!")

@csrf_exempt
def deletefile(request, file_id):
    if request.method == "DELETE":
        File.objects.get(id=file_id).delete()
        return HttpResponse("file deleted!!")


@csrf_exempt
def folderitem(request, folder_id):
    folder = Folder.objects.get(id=folder_id)
    files = File.objects.all().values('id', 'name', 'file', 'created_at')
    return JsonResponse({
        'folder': {
            'id': folder.id,
            'name': folder.name,
            'created_at': folder.created_at
        },
        'files': list(files)
    }, safe=False)