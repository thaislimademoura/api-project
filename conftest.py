import pytest
import requests
import csv
import os
import pytest_html
import allure

# Função para ler CSV
def load_csv_test_cases(path):
    """Reads a CSV file and returns a list of dictionaries."""
    cases = []
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cases.append(row)
    return cases
    
# Fixture que carrega os casos de teste do CSV comments
@pytest.fixture(scope="session")
def comments_test_cases():
    return load_csv_test_cases("comments_test_cases.csv")

# Fixture de sessão: executa uma vez
@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Fixture de função: executa a cada teste
@pytest.fixture(scope="function")
def api_client():
    return requests

# Fixture de sessão: executa uma vez
@pytest.fixture(scope="session")
def httpbin_url():
    return "https://httpbin.org"

