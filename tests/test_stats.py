import pytest
import sys
sys.path.append('/home/steven/so-exam3')

from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client

def test_get_cpu_percent(mocker, client):
  mocker.patch.object(Stats, 'get_porcentaje_cpu', return_value=230)
  response = client.get('/v1/stats/cpu')
  assert response.data.decode('utf-8') == '{"CPU_PORCENT": 230}'
  assert response.status_code == 200

def test_get_available_memory(mocker, client):
  mocker.patch.object(Stats, 'get_memoria_disponible', return_value=500)
  response = client.get('/v1/stats/memory')
  assert response.data.decode('utf-8') == '{"AVAILABLE_MEMORY": 500}'
  assert response.status_code == 200


def test_get_disk_space(mocker, client):
  mocker.patch.object(Stats, 'get_espacio_disco', return_value=2000)
  response = client.get('/v1/stats/disk')
  assert response.data.decode('utf-8') == '{"FREE_DISK": 2000}'
  assert response.status_code == 200

