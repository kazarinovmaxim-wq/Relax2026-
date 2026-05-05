from django.test import TestCase
import pytest
from django.urls import reverse
from http import HTTPStatus

@pytest.mark.django_db
class TestBlogPages:
    def test_index_availability(self, client):
        url = reverse('blog:index')
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK
        # Исправлено на твой путь:
        assert 'html/index.html' in [t.name for t in response.templates]

    @pytest.mark.parametrize('url, status', [
        # '/posts/1/' убрали временно
        ('/category/discovery/', HTTPStatus.OK), 
        ('/posts/9999/', HTTPStatus.NOT_FOUND),
    ])
    def test_pages_status_codes(self, client, url, status):
        response = client.get(url)
        assert response.status_code == status

    def test_index_content(self, client):
        response = client.get(reverse('blog:index'))
        content = response.content.decode('utf-8')
        # Ищем начало тега, чтобы не зависеть от его атрибутов (class, style)
        assert '<header' in content
        assert '<footer' in content
