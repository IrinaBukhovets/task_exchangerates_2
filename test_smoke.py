from ExReAPI import ExReAPI

def test_smoke():
    client_exre = ExReAPI()
    response = client_exre.get_latest('EUR','AED')
    assert response['success'] == True