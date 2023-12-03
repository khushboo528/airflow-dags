from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deploy-1203182411",
}

dag = DAG(
    "model_deploy-1203182411",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_a592cecf_21ed_4efa_8935_ec39c9422b7f = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-1203182411",
    cos_dependencies_archive="build_push_image-a592cecf-21ed-4efa-8935-ec39c9422b7f.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_REGISTRY": "https://index.docker.io/v1",
        "CONTAINER_REGISTRY_USER": "khushbookhushi528",
        "CONTAINER_REGISTRY_PASSWORD": "Mihit@1243",
        "CONTAINER_DETAILS": "khushbookhushi528/mlflowdemo:latest",
    },
    config_file="None",
    dag=dag,
)

notebook_op_a592cecf_21ed_4efa_8935_ec39c9422b7f.image_pull_policy = "IfNotPresent"


notebook_op_0783ea4b_7cc3_4c53_a8ff_70e4b7c4fd7c = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-1203182411",
    cos_dependencies_archive="deploy_model-0783ea4b-7cc3-4c53-a8ff-70e4b7c4fd7c.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/repository/ml-on-k8s/airflow- python-runner",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_DETAILS": "khushbookhushi528/mlflowdemo:latest",
        "CLUSTER_DOMAIN_NAME": "192.168.49.2.nip.io",
    },
    config_file="None",
    dag=dag,
)

notebook_op_0783ea4b_7cc3_4c53_a8ff_70e4b7c4fd7c.image_pull_policy = "IfNotPresent"

(
    notebook_op_0783ea4b_7cc3_4c53_a8ff_70e4b7c4fd7c
    << notebook_op_a592cecf_21ed_4efa_8935_ec39c9422b7f
)
