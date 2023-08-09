import requests
import base64
import zipfile
import io
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def trigger_pipeline_view(request):
    if request.method == 'POST':
        form_data = request.POST
        siemxdr = form_data.get('SIEMxdr')
        monitoring = form_data.get('Monitoring')
        logging = form_data.get('Logging')

        # Replace these variables with your actual GitLab project ID and private token
        project_id = "109"
        private_token = "Brd96ShxJsCfqZsL-3ZB"
        base_url = "https://gitlab.os3.com/api/v4/"
        headers = {"PRIVATE-TOKEN": private_token}

        pipeline_names = []
        if siemxdr:
            pipeline_names.append("SIEMxdr")
            trigger_branch(base_url, project_id, headers, "wazuh-s100")
        if monitoring:
            pipeline_names.append("Monitoring")
            trigger_branch(base_url, project_id, headers, "test")
        if logging:
            pipeline_names.append("Logging")
            trigger_branch(base_url, project_id, headers, "logging")

        return render(request, 'result.html', {'message': 'Installation in Progress', 'pipeline_names': pipeline_names})
    else:
        return render(request, 'trigger_pipeline.html')
    

def trigger_branch(base_url, project_id, headers, branch_name):
    data = {"ref": branch_name}
    response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)

    if response.status_code != 201:
        raise ValueError(f"Error triggering pipeline for branch '{branch_name}': {response.status_code}, {response.json()}")

def get_latest_pipeline_status(base_url, project_id, headers):
    response = requests.get(base_url + f"projects/{project_id}/pipelines", headers=headers, verify=False)

    if response.status_code != 200:
        raise ValueError(f"Error fetching pipelines: {response.status_code}, {response.json()}")

    pipelines = response.json()
    if not pipelines:
        return 'No Pipelines Found'

    latest_pipeline = max(pipelines, key=lambda pipeline: pipeline['created_at'])
    latest_status = latest_pipeline['status']

    return latest_status

def get_latest_pipeline_artifacts(base_url, project_id, headers):
    response = requests.get(base_url + f"projects/{project_id}/pipelines", headers=headers, verify=False)

    if response.status_code != 200:
        raise ValueError(f"Error fetching pipelines: {response.status_code}, {response.json()}")

    pipelines = response.json()
    if not pipelines:
        return []

    latest_pipeline_id = pipelines[0]['id']
    response = requests.get(base_url + f"projects/{project_id}/pipelines/{latest_pipeline_id}/jobs", headers=headers, verify=False)

    if response.status_code != 200:
        raise ValueError(f"Error fetching pipeline jobs: {response.status_code}, {response.json()}")

    jobs = response.json()
    artifacts = []

    for job in jobs:
        response = requests.get(base_url + f"projects/{project_id}/jobs/{job['id']}/artifacts", headers=headers, verify=False)
        if response.status_code == 200:
            # Extract the ip.txt file from the artifacts zip
            with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_file:
                if 'ip.txt' in zip_file.namelist():
                    ip_txt_content = zip_file.read('ip.txt').decode('utf-8')
                    artifacts.append({"filename": "ip.txt", "content": ip_txt_content})

    return artifacts

def get_latest_pipeline_status_and_artifacts(request):
    # Replace these variables with your actual GitLab project ID and private token
    project_id = "109"
    private_token = "Brd96ShxJsCfqZsL-3ZB"
    base_url = "https://gitlab.os3.com/api/v4/"
    headers = {"PRIVATE-TOKEN": private_token}

    # Get the latest pipeline status
    pipeline_status = get_latest_pipeline_status(base_url, project_id, headers)

    # Get the artifacts for the latest pipeline
    artifacts = get_latest_pipeline_artifacts(base_url, project_id, headers)

    return JsonResponse({"status": pipeline_status, "artifacts": artifacts})
