import json

from app import app, ROOT_ENDPOINT_MESSAGE


def test_root_endpoint():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('UTF-8') == ROOT_ENDPOINT_MESSAGE


def test_solve_endpoint_get_request():
    response = app.test_client().get('/solve')

    assert response.status_code == 405


def test_solve_endpoint_empty_post_request():
    response = app.test_client().post('/solve')

    assert response.status_code == 400


def test_solve_endpoint_simple_addition_expression():
    payload = {
        'expression': '2 + 2'
    }
    response = app.test_client().post('/solve', data=json.dumps(payload), content_type='application/json')

    assert response.json['result'] == 4


def test_solve_endpoint_complex_expression():
    payload = {
        'expression': '2 + 2 * 4 + 10 ** 2 - 11 + 8 / 4'
    }
    response = app.test_client().post('/solve', data=json.dumps(payload), content_type='application/json')

    assert response.json['result'] == 101
