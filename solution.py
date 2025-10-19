import pytest
from conftest import load_csv_test_cases  # Caminho correto para importar

test_cases = load_csv_test_cases("test_cases.csv")

# The 'post_test_cases' fixture comes from conftest.py
@pytest.mark.api_test
@pytest.mark.parametrize("test_case", test_cases)
def test_create_post_dynamically(base_url, api_client, test_case):
    """Tests post creation based on data from the CSV."""
    # Prepare the payload data
    payload = {
        "title": test_case["title"],
        "body": test_case["body"],
        "userId": int(test_case["userId"]) if test_case["userId"] else 1
    }
    expected_status = int(test_case["expected_status"])

    # Send the request
    response = api_client.post(f"{base_url}/posts", json=payload)

    # Validate the result
    assert response.status_code == expected_status
    if expected_status == 201:
        assert response.json()["title"] == payload["title"]