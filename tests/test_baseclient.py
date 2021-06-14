import pytest
from pyaws.clients.base import ClientBase

gcloud_credentials_json = 'gcloud.json'

def test_object():
    with pytest.raises(RuntimeError):
        assert ClientBase()
    
def test_s3_connect():
    instant = ClientBase.instance()
    instant.connect(service_name,)
    assert instant._client is not None