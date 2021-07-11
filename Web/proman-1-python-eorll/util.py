from functools import wraps
from flask import jsonify



def json_response(func):
    """
    Converts the returned dictionary into a JSON response
    :param func:
    :return:
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        return jsonify(func(*args, **kwargs))

    return decorated_function


def get_max_id(data):
    id = []

    for i in data:
        id.append(int(i['id']))

    return max(id)