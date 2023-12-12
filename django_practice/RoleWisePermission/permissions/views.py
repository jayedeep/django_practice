from django.shortcuts import render
from django.contrib.auth.models import Permission
# Create your views here.

def list_permissions(request):
    grouped_permissions = {}
    permissions = Permission.objects.all().order_by(
        'content_type__model')
    models = ['user', 'permission', 'group', 'roles']
    for model in models:
        model_permission = permissions.filter(content_type__model=model)
        model_name = model_permission.first().content_type.app_labeled_name.split('|')[-1].strip()
        print(model_name)

        grouped_permissions[model_name] = []
        grouped_permissions[model_name].append(model_permission)
    return render(request, 'permissions/permissions.html',{'grouped_permissions':grouped_permissions})