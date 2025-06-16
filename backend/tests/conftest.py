import os
import pytest
from fastapi.testclient import TestClient
from app.main import app


os.environ["ENV"] = "test" 


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
