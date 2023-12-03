from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-1203174110",
}

dag = DAG(
    "hello_world-1203174110",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_27b24a41_aebf_44da_a223_c2a333490132 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-1203174110",
    cos_dependencies_archive="hello-27b24a41-aebf-44da-a223-c2a333490132.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_27b24a41_aebf_44da_a223_c2a333490132.image_pull_policy = "IfNotPresent"


notebook_op_0d8530b2_8d58_46e9_8512_9df4883c086e = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-1203174110",
    cos_dependencies_archive="world-0d8530b2-8d58-46e9-8512-9df4883c086e.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/repository/ml-on-k8s/airflow- python-runner",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_0d8530b2_8d58_46e9_8512_9df4883c086e.image_pull_policy = "IfNotPresent"

(
    notebook_op_0d8530b2_8d58_46e9_8512_9df4883c086e
    << notebook_op_27b24a41_aebf_44da_a223_c2a333490132
)
