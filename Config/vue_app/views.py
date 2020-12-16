from django.shortcuts import render

# Create your views here.
def test_vue(request):
    return render(request, 'SeniorProject\Client\cassava')