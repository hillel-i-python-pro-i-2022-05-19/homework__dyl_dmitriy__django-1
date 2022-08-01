from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from apps.user_generator.services import generator_of_users


def generate_users_view(request: HttpRequest,
                        users_count: int = 100) -> HttpResponse:
    output_response = generator_of_users(amount_of_users=users_count)
    return render(
        request, 'user_generator/show_users.html',
        {
            "output_response": output_response,
            "users_count": users_count
        }
    )
