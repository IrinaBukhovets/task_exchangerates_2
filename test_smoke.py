from ExReClient import ExReClient

def test_smoke():
    client_requests = ExReClient()
    response = client_requests.requests_exre('BOB')
    assert 'currency_value' in response.keys()
    