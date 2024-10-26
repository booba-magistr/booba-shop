from .models import Carts


def get_user_carts(request):
    if request.user.is_authenticated:
        return Carts.objects.filter(user=request.user).select_related("product")

    if not request.session.session_key:
        request.session.create()
    return Carts.objects.filter(session_key=request.session.session_key).select_related("product")