import os
import pytest
from fastapi.testclient import TestClient
from app.main import app


os.environ["ENV"] = "test"
os.environ["MONGODB_URL"] = "mongodb://localhost:27017"
os.environ["MONGODB_NAME"] = "petdb_test"


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
