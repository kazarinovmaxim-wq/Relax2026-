from django.test import TestCase
import pytest
from django.urls import reverse
from http import HTTPStatus


@pytest.mark.django_db
class TestBlogPages:
    """Комплексная проверка страниц блога"""

    def test_index_availability(self, client):
        """Проверка главной страницы"""
        url = reverse('blog:index')
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK
        # Проверь путь к шаблону, если у тебя html/index.html — замени
        assert 'blog/index.html' in [t.name for t in response.templates]

    @pytest.mark.parametrize('url, status', [
        # Указываем существующий путь или имитируем его
        ('/posts/1/', HTTPStatus.OK),
        ('/category/test-slug/', HTTPStatus.OK),
        # Негативный тест: несуществующий пост
        ('/posts/9999/', HTTPStatus.NOT_FOUND),
    ])
    def test_pages_status_codes(self, client, url, status):
        """Проверка статус-кодов для существующих и битых ссылок"""
        # Мы используем прямые ссылки, чтобы проверить и urls.py
        response = client.get(url)
        assert response.status_code == status

    def test_index_content(self, client):
        """Проверка наличия базовой разметки на главной"""
        response = client.get(reverse('blog:index'))
        content = response.content.decode('utf-8')
        assert '<header>' in content
        assert '<footer>' in content
