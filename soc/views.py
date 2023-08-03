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
import requests
from django.shortcuts import render

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

        if siemxdr:
            trigger_branch(base_url, project_id, headers, "wazuh-s100")
        if monitoring:
            trigger_branch(base_url, project_id, headers, "test")
        if logging:
            trigger_branch(base_url, project_id, headers, "logging")

        return render(request, 'result.html', {'message': 'Pipeline(s) triggered successfully.'})
    else:
        return render(request, 'trigger_pipeline.html')

def trigger_branch(base_url, project_id, headers, branch_name):
    data = {"ref": branch_name}
    response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)

    if response.status_code != 201:
        raise ValueError(f"Error triggering pipeline for branch '{branch_name}': {response.status_code}, {response.json()}")

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
#         return f"{branch_name}: Unable to get pipeline status"

