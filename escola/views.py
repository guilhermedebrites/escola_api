from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        return JsonResponse({'alunos': [
            {'nome': 'João', 'idade': 15},
            {'nome': 'Maria', 'idade': 16},
            {'nome': 'José', 'idade': 16},
        ]})
