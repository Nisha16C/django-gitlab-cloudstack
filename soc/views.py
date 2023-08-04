# # Create your views here.
# # views.py
# from django.shortcuts import render
# from .forms import SOCselection

# def soc_selection_view(request):
#     if request.method == 'POST':
#         form = SOCselection(request.POST)
#         if form.is_valid():
#             form.save()
#             # Do something with the form data (e.g., save to database)
#             # You can also show a success message and redirect the user to another page.
#     else:
#         form = SOCselection()

#     return render(request, 'soc_selection.html', {'form': form})
# views.py
###############################################################################################################


# import requests
# from django.shortcuts import render

# def trigger_pipeline_view(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         siemxdr = form_data.get('SIEMxdr')
#         monitoring = form_data.get('Monitoring')
#         logging = form_data.get('Logging')

#         # Replace these variables with your actual GitLab project ID and private token
#         project_id = "109"
#         private_token = "Brd96ShxJsCfqZsL-3ZB"
#         base_url = "https://gitlab.os3.com/api/v4/"
#         headers = {"PRIVATE-TOKEN": private_token}

#         if siemxdr:
#             trigger_branch(base_url, project_id, headers, "wazuh-s100")
#         if monitoring:
#             trigger_branch(base_url, project_id, headers, "test")
#         if logging:
#             trigger_branch(base_url, project_id, headers, "logging")

#         return render(request, 'result.html', {'message': 'Pipeline(s) triggered successfully.'})
#     else:
#         return render(request, 'trigger_pipeline.html')

# def trigger_branch(base_url, project_id, headers, branch_name):
#     data = {"ref": branch_name}
#     response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)

#     if response.status_code != 201:
#         raise ValueError(f"Error triggering pipeline for branch '{branch_name}': {response.status_code}, {response.json()}")





############################################################################################################################################
# import requests
# from django.shortcuts import render

# def trigger_pipeline_view(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         siemxdr = form_data.get('SIEMxdr')
#         monitoring = form_data.get('Monitoring')
#         logging = form_data.get('Logging')

#         # Replace these variables with your actual GitLab project ID and private token
#         project_id = "109"
#         private_token = "Brd96ShxJsCfqZsL-3ZB"
#         base_url = "https://gitlab.os3.com/api/v4/"
#         headers = {"PRIVATE-TOKEN": private_token}

#         statuses = []
#         if siemxdr:
#             statuses.append(trigger_branch(base_url, project_id, headers, "wazuh-s100"))
#         if monitoring:
#             statuses.append(trigger_branch(base_url, project_id, headers, "test"))
#         if logging:
#             statuses.append(trigger_branch(base_url, project_id, headers, "logging"))

#         return render(request, 'result.html', {'statuses': statuses})
#     else:
#         return render(request, 'trigger_pipeline.html')

# def trigger_branch(base_url, project_id, headers, branch_name):
#     data = {"ref": branch_name}
#     response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)

#     if response.status_code != 201:
#         raise ValueError(f"Error triggering pipeline for branch '{branch_name}': {response.status_code}, {response.json()}")

#     # Get the pipeline ID from the response
#     pipeline_id = response.json().get('id')

#     # Fetch pipeline status using the pipeline ID
#     pipeline_url = f"{base_url}projects/{project_id}/pipelines/{pipeline_id}"
#     response = requests.get(pipeline_url, headers=headers, verify=False)
#     if response.status_code == 200:
#         pipeline_status = response.json().get('status')
#         return f"{branch_name}: {pipeline_status}"
#     else:
#         return f"{branch_name}: Unable to get pipeline status
###############################################################################################################################
# import requests
# import time
# from django.shortcuts import render

# def trigger_pipeline_view(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         siemxdr = form_data.get('SIEMxdr')
#         monitoring = form_data.get('Monitoring')
#         logging = form_data.get('Logging')

#         # Replace these variables with your actual GitLab project ID and private token
#         project_id = "109"
#         private_token = "Brd96ShxJsCfqZsL-3ZB"
#         base_url = "https://gitlab.os3.com/api/v4/"
#         headers = {"PRIVATE-TOKEN": private_token}

#         pipeline_status = {}
#         if siemxdr:
#             pipeline_status["SIEMxdr"] = trigger_branch(base_url, project_id, headers, "wazuh-s100")
#         if monitoring:
#             pipeline_status["Monitoring"] = trigger_branch(base_url, project_id, headers, "test")
#         if logging:
#             pipeline_status["Logging"] = trigger_branch(base_url, project_id, headers, "logging")

#         return render(request, 'result.html', {'message': 'Pipeline(s) triggered successfully.', 'pipeline_status': pipeline_status})
#     else:
#         return render(request, 'trigger_pipeline.html')

# def trigger_branch(base_url, project_id, headers, branch_name):
#     data = {"ref": branch_name}
#     response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)

#     if response.status_code != 201:
#         raise ValueError(f"Error triggering pipeline for branch '{branch_name}': {response.status_code}, {response.json()}")

#     pipeline_id = response.json().get("id")
#     # Wait for a few seconds to let the pipeline start
#     time.sleep(5)

#     pipeline_status = get_pipeline_status(base_url, project_id, headers, pipeline_id)
#     return pipeline_status

# def get_pipeline_status(base_url, project_id, headers, pipeline_id):
#     response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}", headers=headers, verify=False)

#     if response.status_code != 200:
#         raise ValueError(f"Error fetching pipeline status: {response.status_code}, {response.json()}")

#     return response.json().get("status")
################################################
# import requests
# import time
# from django.shortcuts import render
# from django.http import JsonResponse

# def trigger_pipeline_view(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         siemxdr = form_data.get('SIEMxdr')
#         monitoring = form_data.get('Monitoring')
#         logging = form_data.get('Logging')

#         # Replace these variables with your actual GitLab project ID and private token
#         project_id = "109"
#         private_token = "Brd96ShxJsCfqZsL-3ZB"
#         base_url = "https://gitlab.os3.com/api/v4/"
#         headers = {"PRIVATE-TOKEN": private_token}

#         pipeline_status = {}
#         if siemxdr:
#             pipeline_status["SIEMxdr"] = trigger_branch(base_url, project_id, headers, "wazuh-s100")
#         if monitoring:
#             pipeline_status["Monitoring"] = trigger_branch(base_url, project_id, headers, "test")
#         if logging:
#             pipeline_status["Logging"] = trigger_branch(base_url, project_id, headers, "logging")

#         return render(request, 'result.html', {'message': 'Pipeline(s) triggered successfully.', 'pipeline_status': pipeline_status})
#     else:
#         return render(request, 'trigger_pipeline.html')

# def trigger_branch(base_url, project_id, headers, branch_name):
#     data = {"ref": branch_name}
#     response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)

#     if response.status_code != 201:
#         raise ValueError(f"Error triggering pipeline for branch '{branch_name}': {response.status_code}, {response.json()}")

#     pipeline_id = response.json().get("id")
#     # Wait for a few seconds to let the pipeline start
#     time.sleep(5)

#     pipeline_status = get_pipeline_status_by_name(base_url, project_id, headers, pipeline_id)
#     return pipeline_status

# def get_pipeline_status_by_name(base_url, project_id, headers, pipeline_name):
#     response = requests.get(base_url + f"projects/{project_id}/pipelines", headers=headers, verify=False)

#     if response.status_code != 200:
#         raise ValueError(f"Error fetching pipelines: {response.status_code}, {response.json()}")

#     pipelines = response.json()
#     for pipeline in pipelines:
#         if pipeline['id'] == pipeline_name:
#             return pipeline['status']

#     # If the pipeline with the given name is not found, return a default status
#     return 'Not Found'

# def get_pipeline_status(request):
#     pipeline_name = request.GET.get('pipeline_name')

#     # Replace these variables with your actual GitLab project ID and private token
#     project_id = "109"
#     private_token = "Brd96ShxJsCfqZsL-3ZB"
#     base_url = "https://gitlab.os3.com/api/v4/"
#     headers = {"PRIVATE-TOKEN": private_token}

#     # Assuming you have a function to get pipeline status based on the pipeline_name
#     pipeline_status = get_pipeline_status_by_name(base_url, project_id, headers, pipeline_name)

#     return JsonResponse({"status": pipeline_status})

# import requests
# from django.shortcuts import render
# from django.http import JsonResponse

# def trigger_pipeline_view(request):
#     if request.method == 'POST':
#         form_data = request.POST
#         siemxdr = form_data.get('SIEMxdr')
#         monitoring = form_data.get('Monitoring')
#         logging = form_data.get('Logging')

#         # Replace these variables with your actual GitLab project ID and private token
#         project_id = "109"
#         private_token = "Brd96ShxJsCfqZsL-3ZB"
#         base_url = "https://gitlab.os3.com/api/v4/"
#         headers = {"PRIVATE-TOKEN": private_token}

#         pipeline_names = []
#         if siemxdr:
#             pipeline_names.append("SIEMxdr")
#             trigger_branch(base_url, project_id, headers, "wazuh-s100")
#         if monitoring:
#             pipeline_names.append("Monitoring")
#             trigger_branch(base_url, project_id, headers, "test")
#         if logging:
#             pipeline_names.append("Logging")
#             trigger_branch(base_url, project_id, headers, "logging")

#         return render(request, 'result.html', {'message': 'Installation in Progress', 'pipeline_names': pipeline_names})
#     else:
#         return render(request, 'trigger_pipeline.html')

# def trigger_branch(base_url, project_id, headers, branch_name):
#     data = {"ref": branch_name}
#     response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)

#     if response.status_code != 201:
#         raise ValueError(f"Error triggering pipeline for branch '{branch_name}': {response.status_code}, {response.json()}")

# def get_pipeline_status_by_name(base_url, project_id, headers, pipeline_name):
#     response = requests.get(base_url + f"projects/{project_id}/pipelines", headers=headers, verify=False)

#     if response.status_code != 200:
#         raise ValueError(f"Error fetching pipelines: {response.status_code}, {response.json()}")

#     pipelines = response.json()
#     for pipeline in pipelines:
#         if pipeline['ref'] == pipeline_name:
#             return pipeline['status']

#     # If the pipeline with the given name is not found, return a default status
#     return 'Not Found'

# def get_pipeline_status(request):
#     pipeline_name = request.GET.get('pipeline_name')

#     # Replace these variables with your actual GitLab project ID and private token
#     project_id = "109"
#     private_token = "Brd96ShxJsCfqZsL-3ZB"
#     base_url = "https://gitlab.os3.com/api/v4/"
#     headers = {"PRIVATE-TOKEN": private_token}

#     # Get the pipeline status based on the pipeline_name
#     pipeline_status = get_pipeline_status_by_name(base_url, project_id, headers, pipeline_name)

#     return JsonResponse({"status": pipeline_status})
import requests
from django.shortcuts import render
from django.http import JsonResponse


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
            artifacts.append({"filename": job['artifacts_file']['filename']})

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

