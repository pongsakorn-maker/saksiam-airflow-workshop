import logging

from airflow import DAG 
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator


default_args={
    "owner" : "Pongsakorn Maprakhon",
    "start_date": timezone.datetime(2021,9,27)
}
with DAG(
    "homework1_dag",
    schedule_interval="*/10 * * * *",
    default_args=default_args,
    catchup=False,
    tags=["saksiam"],
) as dag:

    first = DummyOperator(task_id="1")
    second = DummyOperator(task_id="2")
    third = DummyOperator(task_id="3")
    fourth = DummyOperator(task_id="4")
    fifth = DummyOperator(task_id="5")
    sixth = DummyOperator(task_id="6")
    seventh = DummyOperator(task_id="7")
    eight = DummyOperator(task_id="8")
    ninth = DummyOperator(task_id="9")

    first >> [second,fifth] >> sixth >> eight >> ninth
    second >> third >> fourth >> ninth
    fifth >> seventh >> eight
