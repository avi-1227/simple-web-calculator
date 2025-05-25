from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    result = None
    operation_name = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get("num1"))
            num2 = float(request.POST.get("num2"))

            if 'add' in request.POST:
                result = int(num1 + num2)
                operation_name = "Addition"
            elif 'sub' in request.POST:
                result = num1 - num2
                operation_name = "Subtraction"
            elif 'multi' in request.POST:
                result = num1 * num2
                operation_name = "Multiplication"
            elif 'div' in request.POST:
                result = "Cannot divided by zero" if num2 == 0 else num1/num2
                operation_name = "Division"
            
        except ValueError:
            result = "Invalid input"

                
    context = {'result':result, 'operation_name':operation_name}

    return render(request, 'calculatorapp/index.html', context)