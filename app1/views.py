from django.shortcuts import render
from .path import make_tree
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def get_tree_path(request):
    try:
        data = make_tree("N4315.H2FI.01")
        # data = make_tree("WR-3203-TN1")
        return Response(data)
    except Exception as e:
        print(f"Exception-->{e}")
        return Response({"is_success": False, "error": str(e)})
