import psutil

class Stats():

  @classmethod
  def get_porcentaje_cpu(cls):
    porcentaje = psutil.cpu_percent()
    return porcentaje

  @classmethod
  def get_memoria_disponible(cls):
    ram = psutil.virtual_memory().available
    return ram

  @classmethod
  def get_espacio_disco(cls):
    espacio = psutil.disk_usage('/').free
    return espacio

