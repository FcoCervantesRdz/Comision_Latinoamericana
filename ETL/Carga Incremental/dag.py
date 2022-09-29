from datetime import timedelta
from email.policy import default
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from cargas_incrementales import carga_incremental_Compromiso
from cargas_incrementales import carga_incremental_datos_ONU
from cargas_incrementales import carga_incremental_energyco2
from cargas_incrementales import carga_incremental_temperatura

#airflow settings
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date':datetime(2022,9,1),
    'email':['jalilpablo@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}
#compromiso
#creating DAG
dag_compromiso = DAG(
    'cargaIncrementalCompromiso',  #name
    default_args=default_args, #args
    description='cargaIncrementalCompromiso',
    schedule="@monthly"
)

carga_inc_compromiso = PythonOperator(
    task_id='carga_incremental_compromiso',
    python_callable=carga_incremental_Compromiso, #what to do
    dag=dag_compromiso #in wich dag
)
carga_inc_compromiso

#datos ONU
#creating DAG
dag_datos_ONU = DAG(
    'cargaIncrementalDatosONU',  #name
    default_args=default_args, #args
    description='cargaIncrementalDatosONU',
    schedule="@monthly"
)

carga_inc_ONU = PythonOperator(
    task_id='carga_incremental_ONU',
    python_callable=carga_incremental_datos_ONU, #what to do
    dag=dag_datos_ONU #in wich dag
)
carga_inc_ONU


#energyCO2
#creating DAG
dag_energyCO2 = DAG(
    'cargaIncrementalEnergyCO2',  #name
    default_args=default_args, #args
    description='cargaIncrementalEnergyCO2',
    schedule="@monthly"
)

carga_inc_energyCO2 = PythonOperator(
    task_id='carga_incremental_enerCO2',
    python_callable=carga_incremental_energyco2, #what to do
    dag=dag_energyCO2 #in wich dag
)
carga_inc_energyCO2


#temperatura
#creating DAG
dag_temperatura = DAG(
    'cargaIncrementalTemp',  #name
    default_args=default_args, #args
    description='cargaIncrementalTemp',
    schedule="@monthly"
)

carga_inc_temp = PythonOperator(
    task_id='carga_incremental_temp',
    python_callable=carga_incremental_temperatura, #what to do
    dag=dag_temperatura #in wich dag
)
carga_inc_temp

