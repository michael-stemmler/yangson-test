import os

import pytest
from yangson import DataModel


@pytest.fixture
def data_model():
    yang_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'yangmodule', 'must-statement'))
    yang_lib = yang_dir + '/yang-library.json'
    return DataModel.from_file(yang_lib, [yang_dir])


def test_must_statement(data_model):
    data = {
        'example-module:c-a': {
            'l-a': [
                {
                    'name': 'A',
                    'identifier': '123:A'
                }
            ]
        },
        'example-module:c-b': {
            'l-b': [
                {
                    'name': 'B1',
                    'identifier': '123:A',
                    'container-a-name': 'A'
                }
            ]
        }
    }

    instance = data_model.from_raw(data)
    instance.validate()


