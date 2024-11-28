from django.shortcuts import redirect
from functools import wraps

def is_leader(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.role == 'LD':
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper