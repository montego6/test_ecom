import json
from django.urls import reverse
import pytest
from rest_framework.test import APIClient


with open("test_requests.json") as file:
    queries = json.load(file)

client = APIClient()


@pytest.mark.parametrize("query", queries)
def test_get_form_view(query):
    response = client.post(reverse("get-form"), query["request"])
    assert response.data == query["response"]
    assert response.status_code == 200
