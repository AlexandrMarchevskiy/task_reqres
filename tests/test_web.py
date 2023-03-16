import pytest
import requests


class TestReqres:
    
    url = "https://reqres.in/"
    
    @pytest.fixture()
    def response(self):
        response = requests.get(self.url)
        return response
    
    def test_status_code(self, response):
        assert response.status_code == 200
    
    def test_home_page_title(self, response):
        assert "Req" in response.text
    
    @pytest.fixture()
    def sample_payload(self):
        payload = {"name": "John", "job": "Software Engineer"}
        return payload
    
    def test_post_request(self, sample_payload):
        response = requests.post(self.url + "api/users", data=sample_payload)
        assert response.status_code == 201
        assert response.json()["name"] == "John"
        assert response.json()["job"] == "Software Engineer"
    

    
    def test_web_request(self, sample_request):
        response = requests.request(sample_request["method"], sample_request["url"], data=sample_request["payload"])
        assert response.status_code == 201
        assert response.json()["name"] == "John"
        assert response.json()["job"] == "Software Engineer"
    
    @pytest.fixture()
    def sample_api_request(self):
        request = {"method": "POST",
                   "url": self.url + "api/users",
                   "payload": {"name": "John", "job": "Software Engineer"}}
        response = requests.request(request["method"], request["url"], data=request["payload"])
        return response
    
    @pytest.fixture()
    def sample_request(self):
        request = {"method": "POST",
                   "url": self.url + "api/users",
                   "payload": {"name": "John", "job": "Software Engineer"}}
        return request
    
    def test_compare_results(self, sample_request, sample_api_request):
        web_response = requests.request(sample_request["method"], sample_request["url"], data=sample_request["payload"])
        
        # Проверка соответствия статус - кода
        assert web_response.status_code == sample_api_request.status_code
        # Проверка соответствия тела ответа
        assert web_response.json() == sample_api_request.json()
