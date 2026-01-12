from django.shortcuts import render


def main_home(request):
    return render(request, "store/main.html")
