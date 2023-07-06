from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def api_users(request, *args, **kwargs):
    # OH
    return Response({"message": "alive"}, status=200)

