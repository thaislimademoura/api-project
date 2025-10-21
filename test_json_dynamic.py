import pytest
from conftest import load_csv_test_cases

# --- QUERY PARAMS ---
# 1. Fetch all comments for post ID 2 and verify that all returned comments belong to that post.
def test_comments_post_id2(api_client, base_url):
    post_id = 2
    response = api_client.get(f"{base_url}/comments", params={"postId": post_id})
    data = response.json()
    assert response.status_code == 200
    assert all(comment["postId"] == post_id for comment in data)
    print("Comment verified")

# 2. List all todos for user ID 5 and verify that the list is not empty.
def test_list_is_not_empty(api_client, base_url):
    user_id = 5
    response = api_client.get(f"{base_url}/todos", params={"userId": user_id})
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    print ("The list is not empty")

# 3. Fetch all albums for user ID 9 and count how many they have (should be 10).
def test_count_albums(api_client, base_url):
    user_id = 9
    response = api_client.get(f"{base_url}/albums", params={"userId": user_id})
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 10
    print (f"The list contains {len(data)} albums")

# 4. List all completed todos (completed: true) for user ID 1 and verify that all in the response are indeed completed.
def test_list_completed_todos(api_client, base_url):
    user_id = 1
    completed_status = True
    response = api_client.get(f"{base_url}/todos", params={"userId": user_id, "completed": completed_status})
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert all(todo["completed"] == True for todo in data)
    print (f"Todo verified")



# --- HEADERS ---
# 5. Send a request to httpbin.org/headers with the custom header X-Custom-Header: MyValue and validate the response.
def test_headers_1(api_client, httpbin_url):
    headers = {"X-Custom-Header": "MyValue"}

    response = api_client.get(f"{httpbin_url}/headers", headers=headers)
    assert response.status_code == 200

    data = response.json()
    headers_received = data.get("headers", {})

    assert headers_received.get("X-Custom-Header") == "MyValue", f"Header not found or incorrect: {headers_received}"
    print("Custom header verified")

# 6. Send a request to httpbin.org/response-headers to set a custom response header (e.g., My-Test-Header: Hello) and check if it is present in the response headers.
def test_headers_2(api_client, httpbin_url):
    # >>>>>> “Quando acessar a URL, quero que a resposta contenha o header My-Test-Header com o valor Hello”.
    response = api_client.get(f"{httpbin_url}/response-headers", params={"My-Test-Header": "Hello"})
    assert response.status_code == 200

    data = response.json()

    assert data.get("My-Test-Header") == "Hello", f"Header not found or incorrect: {data}"
    print("Response headers verified")


# 7. Send a request to httpbin.org/headers with a custom User-Agent header ("My-Test-Agent/1.0") and validate if it was received correctly.
def test_headers_3(api_client, httpbin_url):
    headers = {"User-Agent": "My-test-Agent/1.0"}

    response = api_client.get(f"{httpbin_url}/headers", headers=headers)
    assert response.status_code == 200

    data = response.json()
    headers_received = data.get("headers", {})

    assert headers_received.get("User-Agent") == "My-test-Agent/1.0", f"User-Agent not received correctly: {headers_received}"
    print("User-Agent header verified")


# 8. Send multiple custom headers (X-Header-1: Value1, X-Header-2: Value2) in a single request to httpbin.org/headers and validate all of them.
def test_headers_4(api_client, httpbin_url):
    headers = {"X-Header-1": "Value1",
               "X-Header-2": "Value2"}

    response = api_client.get(f"{httpbin_url}/headers", headers=headers)
    assert response.status_code == 200

    data = response.json()
    headers_received = data.get("headers", {})

    assert headers_received.get("X-Header-1") == "Value1" and headers_received.get("X-Header-2") == "Value2"
    print("Custom headers verified")


# --- AUTHENTICATION ---
# 9. Test the httpbin Basic Auth endpoint (/basic-auth/user/passwd) with the correct credentials (user, passwd) and validate the 200 status.
def test_auth_1(api_client, httpbin_url):
    response = api_client.get(f"{httpbin_url}/basic-auth/user/passwd", auth=('user', 'passwd'))
    assert response.status_code == 200
    data = response.json()
    assert data.get("authenticated") is True # <<< comando adicional de verificação
    assert data.get("user") == "user" # <<< comando adicional de verificação
    print("Correct credentials verified")

# 10. Test the same Basic Auth endpoint with a correct user but wrong password and validate the 401 status.
def test_auth_2(api_client, httpbin_url):
    response = api_client.get(f"{httpbin_url}/basic-auth/user/passwd", auth=('user', 'password'))
    assert response.status_code == 401
    print("Incorrect credentials verified")

# 11. Send a request to httpbin.org/bearer with a valid Bearer Token (mock, e.g., "my-mock-token") and validate the successful authentication.
def test_auth_3(api_client, httpbin_url):
    headers = {"Authorization": "Bearer my-mock-token"}

    response = api_client.get(f"{httpbin_url}/bearer", headers=headers)
    assert response.status_code == 200

    data = response.json()
    assert data.get("authenticated") is True
    print("Successful authentication")

# 12. Send a request to httpbin.org/bearer without any authorization header and validate if the response is 401.
def test_auth_4(api_client, httpbin_url):

    response = api_client.get(f"{httpbin_url}/bearer")
    assert response.status_code == 401
    print("Authentication failure")



# --- ADVANCED ASSERTIONS ---
# 13. Fetch user with ID 1 from JSONPlaceholder and validate the data types of the keys id (int), name (str), address (dict), and company (dict).
def test_assertions_1(api_client, base_url):
    response = api_client.get(f"{base_url}/users/1")
    data = response.json()
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["address"], dict)
    assert isinstance(data["company"], dict)
    assert response.status_code == 200
    print("Validated data types")

# 14. For the same user, check if the address key contains the sub-keys street, city, and zipcode.
def test_assertions_2(api_client, base_url):
    response = api_client.get(f"{base_url}/users/1")
    data = response.json()
    address = data.get("address", {})
    assert response.status_code == 200
    assert "street" in address
    assert "city" in address
    assert "zipcode" in address    
    print("Address countains all sub-keys")

# 15. Fetch post with ID 10 and validate if the keys userId and id are integers and if title and body are non-empty strings.
def test_assertions_3(api_client, base_url):
    response = api_client.get(f"{base_url}/posts/10")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)

    assert isinstance(data["title"], str) and data["title"].strip() != "" # >>> .strip() pra garantir que não contém apenas espaços
    assert isinstance(data["body"], str) and data["body"].strip() != "" # >>> .strip() pra garantir que não contém apenas espaços

    print("Verified conditions")


# 16. List the photos from album with ID 1 and check if each photo in the response contains the keys albumId, id, title, url, and thumbnailUrl.
def test_photos_data(api_client, base_url):
    album_id = 1
    response = api_client.get(f"{base_url}/photos", params={"albumId": album_id})
    data = response.json()
    assert response.status_code == 200
    for photos in data:
        assert "albumId" in photos 
        assert "id" in photos 
        assert "title" in photos 
        assert "url" in photos 
        assert "thumbnailUrl" in photos 
    print ("Photo data verified")

# 17. Check if the email key of user with ID 3 follows a valid email format (contains "@" and "." in the domain part).
def test_valid_email(api_client, base_url):
    response = api_client.get(f"{base_url}/users/3")
    data = response.json()
    assert response.status_code == 200
    email = data.get("email")
    assert "@" in email
    nome, dominio = email.split("@", 1)
    assert "." in dominio
    print (f"The email is valid")

# 18. Fetch the comments for post with ID 5 and check if the list of comments is not empty.
def test_list_comments_not_empty(api_client, base_url):
    post_id = 5
    response = api_client.get(f"{base_url}/comments", params={"postId=5": post_id})
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    print ("The list of comments is not empty")

# 19. For the first comment from the previous list, validate the types of postId (int), id (int), name (str), email (str), and body (str).
def test_valid_data(api_client, base_url):
    post_id = 1
    response = api_client.get(f"{base_url}/comments", params={"postId=1": post_id})
    data = response.json()
    first_comment = data[0]
    assert isinstance(first_comment["postId"], int)
    assert isinstance(first_comment["name"], str)
    assert isinstance(first_comment["email"], str)
    assert isinstance(first_comment["body"], str)
    assert response.status_code == 200
    print("Validated data types")

# 20. Fetch the todo with ID 199 and check if the value of the completed key is a boolean (True or False).
def test_value_boolean(api_client, base_url):
    response = api_client.get(f"{base_url}/todos/199")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data["completed"], bool)
    print (f"Completed key is a boolean")