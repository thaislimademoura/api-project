import requests

#1 --- NEW POST REQUEST ---
def test_new_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "New post",
        "body": "Post content"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    print("Post created")

#2 --- VALIDATE CREATED POST DATA REQUEST ---
def test_validate_post_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "New post",
        "body": "Post content"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    print("Post created")

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

#3 --- UPDATE A POST (PUT) REQUEST ---
def test_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "title": "Update title",
        "body": "Update content"
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    print("Post updated")

#4 --- VALIDATE POST UPDATE (PUT) REQUEST ---
def test_validate_update():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "title": "Update title",
        "body": "Update content"
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    print("Post updated")

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

#5 --- DELETE POST REQUEST ---
def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    print("Post deleted")

#6 --- LIST ALL USERS REQUEST ---
def test_users_list():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 10
    print (f"The list contains {len(data)} users")

#7 --- SPECIFIC USER REQUEST ---
def test_get_specific_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/5")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Chelsey Dietrich"
    print(f"User: {data['name']}")

#8 --- CREATE NEW COMMENT REQUEST ---
def test_new_comment():
    url = "https://jsonplaceholder.typicode.com/posts/1/comments"
    payload = {
        "name": "New comment",
        "email": "user@example.com",
        "body": "Comment content"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    print("Comment created")

#9 --- LIST USER'S ALBUMS ---
def test_users_albums():
    response = requests.get("https://jsonplaceholder.typicode.com/users/3/albums")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data)
    print (f"The list contains {len(data)} albums")

#10 --- LIST PHOTOS IN ALBUM ---
def test_photos_albums():
    response = requests.get("https://jsonplaceholder.typicode.com/albums/2/photos")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data)
    assert not any(photo["title"] == "reprehenderit est deserunt velit ipsam" for photo in data)
    print ("Specific title isn't in the list")

#11 --- CREATE NEW TASK (Todo) REQUEST ---
def test_new_task():
    url = "https://jsonplaceholder.typicode.com/todos"
    payload = {
        "userId": 1,
        "title": "Learn Pytest",
        "completed": False
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    print("Post 'Learn Pytest' created")

#12 --- UPDATE A TASK (PATCH) ---
def test_update_task():
    url = "https://jsonplaceholder.typicode.com/todos/5"
    data = {"completed": True}
    response = requests.put(url, json=data)
    assert response.status_code == 200
    assert response.json().get("completed") is True
    print ("Update task ID 5 completed")

#13 --- LIST USER'S COMPLETED TASKS ---
def test_list_completed_tasks():
    response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true")
    completed = response.json()
    assert response.status_code == 200
    print ("List User's Completed Tasks verified")
    # print (completed)

#14 --- VALIDATE COMMENT'S STRUCTURE ---
def test_validate_comments_structure():
    response = requests.get("https://jsonplaceholder.typicode.com/comments/10")
    data = response.json()
    expected_keys = {"postId", "id", "name", "email", "body"}
    assert response.status_code == 200
    assert expected_keys <= data.keys()
    print(expected_keys)

#15 --- DELETE A COMMENT ---
def test_delete_comment():
    response = requests.delete("https://jsonplaceholder.typicode.com/comments/3")
    assert response.status_code == 200
    print("Comment deleted")

#16 --- CREATE POST WITH INVALID DATA ---
def test_post_invalid_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    print("Post created without data:", data)

#17 --- FETCH SPECIFIC USER'S POSTS ---
def test_fetch_specific_user_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/users/7/posts")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data)
    print (f"The list contains {len(data)} posts")

#18 --- UPDATE USER'S EMAIL (PUT) ---
def test_update_email():
    url = "https://jsonplaceholder.typicode.com/users/2"
    payload = {"email": "new.email@example.com"}
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    print("E-mail updated")

#19: Delete an Album
def test_delete_album():
    response = requests.delete("https://jsonplaceholder.typicode.com/albums/4")
    assert response.status_code == 200
    print("Album deleted")

#20 --- FINAL CHALLENGE WITH JSONPlaceholder ---
def test_final_challenge():
    userId = 1
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "userId": userId,
        "title": "New post",
        "body": "Post content"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    print("Post created")

    post_data = response.json()
    post_id = post_data.get("id")

    comment_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
    payload = {
        "postId": post_id,
        "name": "New comment",
        "email": "user@example.com",
        "body": "Comment content"
    }
    response = requests.post(comment_url, json=payload)
    assert response.status_code == 201
    print("Comment created")

    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200
    print("Post deleted")
    