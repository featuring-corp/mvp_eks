from django.http import JsonResponse


def get_status(request):
    return JsonResponse({"jake": 'test'}, status=200)
