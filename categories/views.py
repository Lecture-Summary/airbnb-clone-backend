from django.http import JsonResponse
from .models import Category


def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse({"ok": True, "all_categories": all_categories})
