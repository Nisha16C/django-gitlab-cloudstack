# # import requests

# # GITLAB_API_URL = 'https://gitlab.os3.com/api/v4/'
# # PRIVATE_TOKEN = 'Fx1nwyyykeumx9TFgFmS'
# # PROJECT_ID = '100'
# # BRANCH_NAME = 'vulnerbilityfix'  # Replace with the branch name

# # headers = {
# #     'PRIVATE-TOKEN': PRIVATE_TOKEN

# # }

# # job_names = ['code_quality']  # Replace with the names of the jobs you want to trigger

# # for job_name in job_names:
# #     data = {
# #         'ref': BRANCH_NAME,
# #         'variables': {
# #             'CI_JOB_NAME': job_name,
# #         },
# #     }

# #     response = requests.post(f'{GITLAB_API_URL}/projects/{PROJECT_ID}/pipeline', json=data, headers=headers, verify=False)

# #     if response.status_code == 201:
# #         print(f'Job "{job_name}" triggered successfully')
# #     else:
# #         print(f'Failed to trigger job "{job_name}":', response.text)
# # # import requests

# # # # GitLab API variables
# # # GITLAB_URL = 'https://gitlab.os3.com/api/v4/'  # Update this to your GitLab instance URL
# # # PROJECT_ID = '100'  # Replace with your GitLab project's ID
# # # JOB_TOKEN = 'Fx1nwyyykeumx9TFgFmS'  # Replace with your job trigger token
# # # JOB_NAME = 'code_quality'  # Replace with the name of the job you want to trigger

# # # def trigger_job():
# # #     headers = {
# # #         'PRIVATE-TOKEN': JOB_TOKEN
# # #     }
    
# # #     # API endpoint to trigger a specific job
# # #     endpoint = f'{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/trigger/pipeline'
    
# # #     payload = {
# # #         'token': JOB_TOKEN,
# # #         'ref': 'vulnerbilityfix',  # Branch name where the job is defined
# # #         'variables[JOB_NAME]': 'true'  # Set a variable with the job name to trigger it
# # #     }
    
# # #     response = requests.post(endpoint, headers=headers, json=payload, verify=False)
    
# # #     if response.status_code == 201:
# # #         print(f'Job "{JOB_NAME}" triggered successfully!')
# # #     else:
# # #         print(f'Failed to trigger job. Status code: {response.status_code}')
# # #         print(response.text)

# # # if __name__ == '__main__':
# # #     trigger_job()
# import requests
# import json

# # GitLab API endpoint URL
# gitlab_api_url = "https://gitlab.os3.com/api/v4"

# # Your GitLab access token
# access_token = "Fx1nwyyykeumx9TFgFmS"

# # Project ID and branch name
# project_id = 100
# branch_name = "vulnerbilityfix"
# job_name_to_trigger = "code_quality"  # Name of the manual job you want to trigger

# # Define headers
# headers = {
#     "Content-Type": "application/json",
#     "PRIVATE-TOKEN": access_token
# }

# # Get the latest pipeline for the specified branch
# pipeline_url = f"{gitlab_api_url}/projects/{project_id}/pipelines?ref={branch_name}"
# response = requests.get(pipeline_url, headers=headers, verify=False)

# if response.status_code == 200:
#     pipelines = response.json()
#     if pipelines:
#         latest_pipeline = pipelines[0]  # Get the latest pipeline
#         jobs_url = latest_pipeline["jobs"]["pipeline_jobs_url"]

#         # Get the list of jobs in the pipeline
#         response = requests.get(jobs_url, headers=headers)
#         if response.status_code == 200:
#             jobs = response.json()
            
#             # Find the manual job by name
#             for job in jobs:
#                 if job["status"] == "manual" and job["name"] == job_name_to_trigger:
#                     job_id = job["id"]
#                     print(f"Triggering manual job with name '{job_name_to_trigger}' and ID {job_id}")
                    
#                     # Trigger the manual job
#                     trigger_url = f"{gitlab_api_url}/projects/{project_id}/jobs/{job_id}/play"
#                     response = requests.post(trigger_url, headers=headers, verify=False)
                    
#                     if response.status_code == 200:
#                         print("Job triggered successfully!")
#                     else:
#                         print("Failed to trigger the job. Status code:", response.status_code)
#                     break  # Stop after triggering the specified manual job
#             else:
#                 print(f"No manual job found with name '{job_name_to_trigger}' in the pipeline.")
#         else:
#             print("Failed to get job list. Status code:", response.status_code)
#     else:
#         print(f"No pipelines found for branch '{branch_name}'.")
# else:
#     print("Failed to get pipeline information. Status code:", response.status_code)
import requests
import json

# GitLab API endpoint URL
gitlab_api_url = "https://gitlab.os3.com/api/v4"

# Your GitLab access token
access_token = "Brd96ShxJsCfqZsL-3ZB"

# Project ID and branch name
project_id = 109
branch_name = "wazuh-s100"

# List of manual job names to trigger
job_names_to_trigger = ["Dev:validate"]

# Define headers
headers = {
    "Content-Type": "application/json",
    "PRIVATE-TOKEN": access_token
}

# Get the latest pipeline for the specified branch
pipeline_url = f"{gitlab_api_url}/projects/{project_id}/pipelines?ref={branch_name}"
response = requests.get(pipeline_url, headers=headers, verify=False)
print("API Response:")
print(response.text)
if response.status_code == 200:
    pipelines = response.json()
    if pipelines:
        latest_pipeline = pipelines[0]  # Get the latest pipeline
        
        # Check if the 'jobs' key exists in the response
        if 'jobs' in latest_pipeline:
            jobs_url = latest_pipeline["jobs"]["pipeline_jobs_url"]

            # Get the list of jobs in the pipeline
            response = requests.get(jobs_url, headers=headers)
            if response.status_code == 200:
                jobs = response.json()
                
                # Trigger the specified manual jobs by name
                for job_name in job_names_to_trigger:
                    for job in jobs:
                        if job["status"] == "manual" and job["name"] == job_name:
                            job_id = job["id"]
                            print(f"Triggering manual job with name '{job_name}' and ID {job_id}")
                            
                            # Trigger the manual job
                            trigger_url = f"{gitlab_api_url}/projects/{project_id}/jobs/{job_id}/play"
                            response = requests.post(trigger_url, headers=headers)
                            
                            if response.status_code == 200:
                                print("Job triggered successfully!")
                            else:
                                print("Failed to trigger the job. Status code:", response.status_code)
                            break  # Stop after triggering the specified manual job
                    else:
                        print(f"No manual job found with name '{job_name}' in the pipeline.")
            else:
                print("Failed to get job list. Status code:", response.status_code)
        else:
            print("No 'jobs' key found in the pipeline response.")
    else:
        print(f"No pipelines found for branch '{branch_name}'.")
else:
    print("Failed to get pipeline information. Status code:", response.status_code)
