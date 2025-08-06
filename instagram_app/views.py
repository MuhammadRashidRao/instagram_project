from django.shortcuts import render, redirect
from django.db import connection

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                [username, password, email]
            )
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE username = %s AND password = %s",
                [username, password]
            )
            user = cursor.fetchone()
            if user:
                return redirect('home')
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')
