from models import db, MaintenanceLog


def test_add_log(client):
    response = client.post('/add', data={
        'part': 'test part',
        'mileage': 1000,
        'notes': 'test notes'
    }, follow_redirects=False)
    assert response.status_code == 302  # redirect to index
    with client.application.app_context():
        count = MaintenanceLog.query.count()
        assert count == 1


def test_list_logs(client):
    # add an entry first
    client.post('/add', data={'part': 'oil', 'mileage': 100, 'notes': ''})
    response = client.get('/')
    assert response.status_code == 200
    assert b'oil' in response.data


def test_invalid_input(client):
    response = client.post('/add', data={'part': '', 'mileage': 50, 'notes': ''})
    assert response.status_code == 200  # form re-rendered due to validation error
    with client.application.app_context():
        assert MaintenanceLog.query.count() == 0
