from django.test import TestCase
import pytest
from django.urls import reverse
from http import HTTPStatus

@pytest.mark.parametrize('name, template', [
    ('pages:about', 'pages/about.html'),
    ('pages:rules', 'pages/rules.html'),
])
def test_static_pages_availability_and_template(client, name, template):
    """Проверка доступности и используемых шаблонов статических страниц"""
    url = reverse(name)
    response = client.get(url)
    
    # Проверяем статус-код 200
    assert response.status_code == HTTPStatus.OK, f'Страница {url} недоступна'
    
    # Проверяем, что используется верный шаблон
    assert template in [t.name for t in response.templates], (
        f'Для страницы {url} используется неверный шаблон'
    )
