import requests

# --- QUERY PARAMS ---
# 1. Fetch all comments for post ID 2 and verify that all returned comments belong to that post.
def test_comments_post_id2():
    response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=2")
    data = response.json()
    assert response.status_code == 200
    assert all(comment["postId"] == 2 for comment in data)
    print("Comment verified")

# 2. List all todos for user ID 5 and verify that the list is not empty.
def test_list_is_not_empty():
    response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=5")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    print ("The list is not empty")

# 3. Fetch all albums for user ID 9 and count how many they have (should be 10).
def test_count_albums():
    response = requests.get("https://jsonplaceholder.typicode.com/albums?userId=9")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 10
    print (f"The list contains {len(data)} albums")

# 4. List all completed todos (completed: true) for user ID 1 and verify that all in the response are indeed completed.
def test_list_completed_todos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert all(todo["completed"] == True for todo in data)
    print (f"Todos verified")



# --- HEADERS ---
# 5. Send a request to httpbin.org/headers with the custom header X-Custom-Header: MyValue and validate the response.
def test_headers_1():
    url = "https://httpbin.org/headers"
    headers = {"X-Custom-Header": "MyValue"}

    response = requests.get(url, headers=headers)
    assert response.status_code == 200

    data = response.json()
    headers_received = data.get("headers", {})

    assert headers_received.get("X-Custom-Header") == "MyValue", f"Header not found or incorrect: {headers_received}"
    print("Custom header verified")

# 6. Send a request to httpbin.org/response-headers to set a custom response header (e.g., My-Test-Header: Hello) and check if it is present in the response headers.

# 7. Send a request to httpbin.org/headers with a custom User-Agent header ("My-Test-Agent/1.0") and validate if it was received correctly.

# 8. Send multiple custom headers (X-Header-1: Value1, X-Header-2: Value2) in a single request to httpbin.org/headers and validate all of them.





# --- AUTHENTICATION ---
# 9. Test the httpbin Basic Auth endpoint (/basic-auth/user/passwd) with the correct credentials (user, passwd) and validate the 200 status.

# 10. Test the same Basic Auth endpoint with a correct user but wrong password and validate the 401 status.

# 11. Send a request to httpbin.org/bearer with a valid Bearer Token (mock, e.g., "my-mock-token") and validate the successful authentication.

# 12. Send a request to httpbin.org/bearer without any authorization header and validate if the response is 401.




# --- ADVANCED ASSERTIONS ---
# 13. Fetch user with ID 1 from JSONPlaceholder and validate the data types of the keys id (int), name (str), address (dict), and company (dict).

# 14. For the same user, check if the address key contains the sub-keys street, city, and zipcode.

# 15. Fetch post with ID 10 and validate if the keys userId and id are integers and if title and body are non-empty strings.

# 16. List the photos from album with ID 1 and check if each photo in the response contains the keys albumId, id, title, url, and thumbnailUrl.

# 17. Check if the email key of user with ID 3 follows a valid email format (contains "@" and "." in the domain part).

# 18. Fetch the comments for post with ID 5 and check if the list of comments is not empty.

# 19. For the first comment from the previous list, validate the types of postId (int), id (int), name (str), email (str), and body (str).

# 20. Fetch the todo with ID 199 and check if the value of the completed key is a boolean (True or False).