import pytest
from conftest import load_csv_test_cases

comments_test_cases = load_csv_test_cases("comments_test_cases.csv")

@pytest.mark.parametrize("test_case", comments_test_cases)
def test_comments_post_id_dynamic(test_case, api_client, base_url):
    post_id = int(test_case["postId"])
    expected_status = int(test_case["expected_status"])

    response = api_client.get(f"{base_url}/comments", params={"postId": post_id})
    data = response.json()

    assert response.status_code == expected_status
    assert all(comment["postId"] == post_id for comment in data)
