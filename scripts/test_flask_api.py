import pytest
import requests
import json

BASE_URL = "http://localhost:5000"  # Replace with deployed URL in production

def log_response_errors(response, endpoint_name):
    if response.status_code != 200:
        print(f"\n [{endpoint_name}] Failed with status code {response.status_code}")
        try:
            print("🔍 Error Message:", response.json())
        except Exception:
            print("🔍 Raw Response Text:", response.text)

def test_predict_endpoint():
    data = {
        "comments": ["This is a good product!", "Not worth the money.", "It's okay."]
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    log_response_errors(response, "predict")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_predict_with_timestamps_endpoint():
    data = {
        "comments": [
            {"text": "This is fantastic!", "timestamp": "2024-10-25 10:00:00"},
            {"text": "Could be better.", "timestamp": "2024-10-26 14:00:00"}
        ]
    }
    response = requests.post(f"{BASE_URL}/predict_with_timestamps", json=data)
    log_response_errors(response, "predict_with_timestamps")
    
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)
    assert all(isinstance(item, dict) and 'sentiment' in item for item in response_json)

def test_generate_chart_endpoint():
    data = {
        "sentiment_counts": {"1": 5, "0": 3, "-1": 2}
    }
    response = requests.post(f"{BASE_URL}/generate_chart", json=data)
    log_response_errors(response, "generate_chart")
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"

def test_generate_wordcloud_endpoint():
    data = {
        "comments": ["Love this!", "Not so great.", "Absolutely amazing!", "Horrible experience."]
    }
    response = requests.post(f"{BASE_URL}/generate_wordcloud", json=data)
    log_response_errors(response, "generate_wordcloud")
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"

def test_generate_trend_graph_endpoint():
    data = {
        "sentiment_data": [
            {"timestamp": "2024-10-01", "sentiment": 1},
            {"timestamp": "2024-10-02", "sentiment": 0},
            {"timestamp": "2024-10-03", "sentiment": -1}
        ]
    }
    response = requests.post(f"{BASE_URL}/generate_trend_graph", json=data)
    log_response_errors(response, "generate_trend_graph")
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"
