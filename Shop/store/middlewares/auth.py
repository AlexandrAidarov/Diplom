from django.shortcuts import redirect


def auth_middleware(get_response):
    def middleware(request):
        if request.path == "/login" or request.path == "/signup" or request.path == "/verify" or request.path == "/forgot-password" or request.path == "/reset-password" or request.path == "/cart" or request.path == "/":
            return get_response(request)
        customer = request.session.get('customer')
        if not customer:
            return redirect('/login')
        return get_response(request)
    return middleware