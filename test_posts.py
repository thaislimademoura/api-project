import pytest
from conftest import load_csv_test_cases

test_cases = load_csv_test_cases("test_cases.csv")

@pytest.mark.api_test 
@pytest.mark.parametrize("test_case", test_cases)
def test_create_post_dynamically(base_url, api_client, test_case):
    """Testa criação de post usando dados do CSV."""

    # Preparar dados do payload para o POST
    payload = {
        "title": test_case["title"],
        "body": test_case["body"],
        "userId": int(test_case["userId"]) if test_case["userId"] else 1
    }
    expected_status = int(test_case["expected_status"])

    # Fazer a requisição POST
    response = api_client.post(f"{base_url}/posts", json=payload)

    # Validar resultado
    assert response.status_code == expected_status
    if expected_status == 201:
        assert response.json()["title"] == payload["title"]
