from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

def carga_incremental_Compromiso(Compromiso_nuevo):
  #credenciales y cliente
  credentials = service_account.Credentials.from_service_account_file('...') #credenciales
  project_id = 'tidy-hold-359719' #nombre del proyecto
  client = bigquery.Client(credentials= credentials,project=project_id)
  # imprimo valores actuales de la tabla a actualizar
  table_id = "tidy-hold-359719.comision_latinoamericana.Compromiso"
  table = client.get_table(table_id)  # Make an API request.
  print("La tabla tenia originalmente {} filas y {} columnas".format(table.num_rows, len(table.schema)))

  #cargo tabla a actualizar
  q_Compromiso_viejo="""SELECT * FROM `tidy-hold-359719.comision_latinoamericana.Compromiso`"""   #query para tabla NDC
  Compromiso_viejo = client.query(q_Compromiso_viejo).to_dataframe() #dataframe de NDC

  #tabla vacia con la estructura de la tabla a actualizar, aca se cargan las filas nuevas
  filas_a_cargar = Compromiso_viejo.truncate(after=-1)
  
  nuevo = Compromiso_nuevo[['Pais','Anio']].values.tolist() #Anio y Pais de la tabla con valores nuevos
  viejo = Compromiso_viejo[['Pais','Anio']].values.tolist() #Anio y Pais de la tabla a actualizar

  #si el conjunto anio pais de la tabla nueva no esta en la tabla vieja, anexa la fila a la tabla a cargar
  for i in nuevo:
    if i not in viejo:
      filas_a_cargar=filas_a_cargar.append(Compromiso_nuevo[(Compromiso_nuevo.Pais==i[0]) & (Compromiso_nuevo.Anio==i[1])])
  

  #configuracion de la carga
  job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
  job = client.load_table_from_dataframe(filas_a_cargar, table_id, job_config=job_config)  
  # Make an API request.
  job.result()  # Wait for the job to complete.
  table = client.get_table(table_id)  # Make an API request.
  print("Ahora tiene {} filas".format(table.num_rows))


def carga_incremental_datos_ONU(datos_ONU_nuevo):
  #credenciales y cliente
  credentials = service_account.Credentials.from_service_account_file('...') #credenciales
  project_id = 'tidy-hold-359719' #nombre del proyecto
  client = bigquery.Client(credentials= credentials,project=project_id)
  # imprimo valores actuales de la tabla a actualizar
  table_id = "tidy-hold-359719.comision_latinoamericana.datos_ONU"
  table = client.get_table(table_id)  # Make an API request.
  print("La tabla tenia originalmente {} filas y {} columnas".format(table.num_rows, len(table.schema)))

  #cargo tabla a actualizar
  q_datos_ONU_viejo="""SELECT * FROM `tidy-hold-359719.comision_latinoamericana.datos_ONU`"""   #query para tabla NDC
  datos_ONU_viejo = client.query(q_datos_ONU_viejo).to_dataframe() #dataframe de NDC

  #tabla vacia con la estructura de la tabla a actualizar, aca se cargan las filas nuevas
  filas_a_cargar = datos_ONU_viejo.truncate(after=-1)
  
  nuevo = datos_ONU_nuevo[['Pais','Anio']].values.tolist() #Anio y Pais de la tabla con valores nuevos
  viejo = datos_ONU_viejo[['Pais','Anio']].values.tolist() #Anio y Pais de la tabla a actualizar

  #si el conjunto anio pais de la tabla nueva no esta en la tabla vieja, anexa la fila a la tabla a cargar
  for i in nuevo:
    if i not in viejo:
      filas_a_cargar=filas_a_cargar.append(datos_ONU_nuevo[(datos_ONU_nuevo.Pais==i[0]) & (datos_ONU_nuevo.Anio==i[1])])
  

  #configuracion de la carga
  job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
  job = client.load_table_from_dataframe(filas_a_cargar, table_id, job_config=job_config)  
  # Make an API request.
  job.result()  # Wait for the job to complete.
  table = client.get_table(table_id)  # Make an API request.
  print("Ahora tiene {} filas".format(table.num_rows))




def carga_incremental_energyco2(energyco2_nuevo):
  #credenciales y cliente
  credentials = service_account.Credentials.from_service_account_file('...') #credenciales
  project_id = 'tidy-hold-359719' #nombre del proyecto
  client = bigquery.Client(credentials= credentials,project=project_id)
  # imprimo valores actuales de la tabla a actualizar
  table_id = "tidy-hold-359719.comision_latinoamericana.energyco2"
  table = client.get_table(table_id)  # Make an API request.
  print("La tabla tenia originalmente {} filas y {} columnas".format(table.num_rows, len(table.schema)))

  #cargo tabla a actualizar
  q_energyco2_viejo="""SELECT * FROM `tidy-hold-359719.comision_latinoamericana.energyco2`"""   #query para tabla NDC
  energyco2_viejo = client.query(q_energyco2_viejo).to_dataframe() #dataframe de NDC

  #tabla vacia con la estructura de la tabla a actualizar, aca se cargan las filas nuevas
  filas_a_cargar = energyco2_viejo.truncate(after=-1)
  
  nuevo = energyco2_nuevo[['Pais','Anio']].values.tolist() #Anio y Pais de la tabla con valores nuevos
  viejo = energyco2_viejo[['Pais','Anio']].values.tolist() #Anio y Pais de la tabla a actualizar

  #si el conjunto anio pais de la tabla nueva no esta en la tabla vieja, anexa la fila a la tabla a cargar
  for i in nuevo:
    if i not in viejo:
      filas_a_cargar=filas_a_cargar.append(energyco2_nuevo[(energyco2_nuevo.Pais==i[0]) & (energyco2_nuevo.Anio==i[1])])
  

  #configuracion de la carga
  job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
  job = client.load_table_from_dataframe(filas_a_cargar, table_id, job_config=job_config)  
  # Make an API request.
  job.result()  # Wait for the job to complete.
  table = client.get_table(table_id)  # Make an API request.
  print("Ahora tiene {} filas".format(table.num_rows))

def carga_incremental_temperatura(temperatura_nuevo):
  #credenciales y cliente
  credentials = service_account.Credentials.from_service_account_file('...') #credenciales
  project_id = 'tidy-hold-359719' #nombre del proyecto
  client = bigquery.Client(credentials= credentials,project=project_id)
  # imprimo valores actuales de la tabla a actualizar
  table_id = "tidy-hold-359719.comision_latinoamericana.temperatura"
  table = client.get_table(table_id)  # Make an API request.
  print("La tabla tenia originalmente {} filas y {} columnas".format(table.num_rows, len(table.schema)))

  #cargo tabla a actualizar
  q_temperatura_viejo="""SELECT * FROM `tidy-hold-359719.comision_latinoamericana.temperatura`"""   #query para tabla NDC
  temperatura_viejo = client.query(q_temperatura_viejo).to_dataframe() #dataframe de NDC

  #tabla vacia con la estructura de la tabla a actualizar, aca se cargan las filas nuevas
  filas_a_cargar = temperatura_viejo.truncate(after=-1)
  
  nuevo = temperatura_nuevo[['Pais','Cod_Pais']].values.tolist() #Cod_Pais y Pais de la tabla con valores nuevos
  viejo = temperatura_viejo[['Pais','Cod_Pais']].values.tolist() #Cod_Pais y Pais de la tabla a actualizar

  #si el conjunto Cod_Pais pais de la tabla nueva no esta en la tabla vieja, anexa la fila a la tabla a cargar
  for i in nuevo:
    if i not in viejo:
      filas_a_cargar=filas_a_cargar.append(temperatura_nuevo[(temperatura_nuevo.Pais==i[0]) & (temperatura_nuevo.Cod_Pais==i[1])])
  

  #configuracion de la carga
  job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
  job = client.load_table_from_dataframe(filas_a_cargar, table_id, job_config=job_config)  
  # Make an API request.
  job.result()  # Wait for the job to complete.
  table = client.get_table(table_id)  # Make an API request.
  print("Ahora tiene {} filas".format(table.num_rows))
