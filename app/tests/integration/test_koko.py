import json

def test_koko(test_app,test_database):
    client = test_app.test_client()
    resp = client.get("/koko/")
    data = json.loads((resp.data.decode()))
    assert resp.status_code == 200
    assert data['total_amount'] is int