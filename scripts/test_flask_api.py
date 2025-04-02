import pytest
import requests
import json
import os

BASE_URL = "http://localhost:5000"

def test_predict_endpoint():
    data = {
        "comments": ["This is a great product!", "Not worth the money.", "It's okay."]
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    assert isinstance(response.json(), list), "Response is not a list. Response: {response.text}"

def test_predict_with_timestamps_endpoint():
    data = {
        "comments": [
            {"text": "This is fantastic!", "timestamp": "2024-10-25 10:00:00"},
            {"text": "Could be better.", "timestamp": "2024-10-26 14:00:00"}
        ]
    }
    response = requests.post(f"{BASE_URL}/predict_with_timestamps", json=data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    response_json = response.json()
    assert isinstance(response_json, list), f"Response is not a list. Response: {response.text}"
    assert all('sentiment' in item for item in response_json), "Missing 'sentiment' key in response. Response: {response.text}"

def test_generate_chart_endpoint():
    data = {
        "sentiment_counts": {"1": 5, "0": 3, "-1": 2}
    }
    response = requests.post(f"{BASE_URL}/generate_chart", json=data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    assert response.headers.get("Content-Type") == "image/png", f"Expected image/png, got {response.headers.get('Content-Type')}"

def test_generate_wordcloud_endpoint():
    data = {
        "comments": ["Love this!", "Not so great.", "Absolutely amazing!", "Horrible experience."]
    }
    response = requests.post(f"{BASE_URL}/generate_wordcloud", json=data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    assert response.headers.get("Content-Type") == "image/png", f"Expected image/png, got {response.headers.get('Content-Type')}"

def test_generate_trend_graph_endpoint():
    data = {
        "sentiment_data": [
            {"timestamp": "2024-10-01", "sentiment": 1},
            {"timestamp": "2024-10-02", "sentiment": 0},
            {"timestamp": "2024-10-03", "sentiment": -1}
        ]
    }
    response = requests.post(f"{BASE_URL}/generate_trend_graph", json=data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
    assert response.headers.get("Content-Type") == "image/png", f"Expected image/png, got {response.headers.get('Content-Type')}"
