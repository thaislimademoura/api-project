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
        "title": "New comment",
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
    assert data[0]['title'] == "reprehenderit est deserunt velit ipsam"
    print ("Name of the first photo verified")