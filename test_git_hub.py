import requests
 
#1 --- REQUISIÇÃO SIMPLES ---
def test_simple_request():
    response = requests.get("https://api.github.com/")
    assert response.status_code == 200
    
#2 --- REQUISIÇÃO USER ---
def test_get_specific_user():
    response = requests.get("https://api.github.com/users/octocat")
    data = response.json()
    assert response.status_code == 200
    assert data["login"] == "octocat"
    print(f"User: {data['login']}")

#3 --- REQUISIÇÃO TYPE ---
def test_get_type_user():
    response = requests.get("https://api.github.com/users/octocat")
    data = response.json()
    assert response.status_code == 200
    assert data["type"] == "User"
    print(f"Type: '{data['type']}'")

#4 --- REQUISIÇÃO REPOSITORY ID ---
def test_get_repository_id():
    response = requests.get("https://api.github.com/repositories/1296269")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1296269 
    assert data["name"] == "Hello-World"

#5 --- REQUISIÇÃO HANDLING ERRORS ---
def test_non_existent_user():
    response = requests.get("https://api.github.com/users/nonexistentuser12345")
    data = response.json()
    assert response.status_code == 404
    assert data["message"] == "Not Found"

#6 --- REQUISIÇÃO LIST USER REPOSITORIES ---
def test_list_user_repository():
    response = requests.get("https://api.github.com/users/google/repos?per_page=5")
    data = response.json()
    assert response.status_code == 200
    print(f"First Repository Name: '{data[0]['name']}'")

# 7 --- REQUISIÇÃO NAVIGATE FOLLOWER PAGINATION ---
def test_navigate_follower_pagination():
    response = requests.get("https://api.github.com/users/microsoft/followers")
    next_page_link = response.links["next"]["url"]
    print("Next Page:", next_page_link)
    response_page_2 = requests.get(next_page_link)
    assert response_page_2.status_code == 200

#8 --- REQUISIÇÃO COUNT A USER'S PUBLIC REPOSITORIES ---
def test_count_users_public_repositories():
    response = requests.get("https://api.github.com/users/facebook")
    data = response.json()
    assert response.status_code == 200
    print(f"Number of Public Repositories: {data['public_repos']}")

#9 --- REQUISIÇÃO FIND SPECIFIC LANGUAGE IN A REPOSITORY ---
def test_specific_language():
    response = requests.get("https://api.github.com/repos/facebook/react/languages")
    data = response.json()
    assert response.status_code == 200
    assert "JavaScript" in data
    print ('"JavaScript" is in the list')

#10 --- REQUISIÇÃO EXPLORE ANOTHER ENDPOINT (EMOJIS) ---
def test_list_emojis():
    response = requests.get("https://api.github.com/emojis")
    data = response.json()
    assert response.status_code == 200
    assert "+1" in data
    print ('Emoji "+1" found in the list')