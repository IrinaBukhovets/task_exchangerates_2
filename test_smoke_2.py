from ExReClient import ExReClient



def test_smoke():

    client_requests_1 = ExReClient()
    response_1 = client_requests_1.requests_exre('BOB')
    client_requests_2 = ExReClient()
    response_2 = client_requests_2.requests_exre('BOB')
    assert response_1["timestamp"] == response_2["timestamp"]