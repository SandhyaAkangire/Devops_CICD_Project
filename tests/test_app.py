from app.main import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"DevOps CI/CD Project is running!" in response.data


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200


def test_version():
    response = app.test_client().get("/version")
    assert response.status_code == 200