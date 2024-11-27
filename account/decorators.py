from django.shortcuts import redirect

def is_company(view_func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect('dashboard')
        return view_func()
    return wrapper
