from django.shortcuts import render

def sumar_view(request):
    resultado = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        resultado = num1 + num2
    return render(request, 'mi_app/sumar.html', {'resultado': resultado})