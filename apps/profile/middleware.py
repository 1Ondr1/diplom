from django.utils.timezone import now

class UpdateLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user = request.user
            user.last_seen = now()
            user.save(update_fields=['last_seen'])
        response = self.get_response(request)
        return response
