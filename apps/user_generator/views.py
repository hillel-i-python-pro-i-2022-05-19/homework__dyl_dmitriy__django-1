from typing import ClassVar

from django.views.generic import TemplateView

from apps.user_generator.services import generator_of_users


class GenerateUsersView(TemplateView):
    template_name = 'user_generator/show_users.html'

    _DEFAULT_USERS_COUNT: ClassVar[int] = 100

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        try:
            users_count = data['users_count']
        except KeyError:
            users_count = self._DEFAULT_USERS_COUNT

        generated_users_list = generator_of_users(amount_of_users=users_count)

        data['generated_users_list'] = generated_users_list

        return data
