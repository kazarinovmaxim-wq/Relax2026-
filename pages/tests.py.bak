from django.test import TestCase
import pytest
from django.urls import reverse
from http import HTTPStatus

@pytest.mark.parametrize('name, template', [
    ('pages:about', 'html/about.html'),  # Заменили путь на твой реальный
    ('pages:rules', 'html/rules.html'),  # Заменили путь на твой реальный
])
def test_static_pages_availability_and_template(client, name, template):
    url = reverse(name)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert template in [t.name for t in response.templates]
