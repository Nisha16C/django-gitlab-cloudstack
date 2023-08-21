import requests

GITLAB_API_URL = 'https://gitlab.os3.com/api/v4/'
PRIVATE_TOKEN = 'Fx1nwyyykeumx9TFgFmS'
PROJECT_ID = '100'
BRANCH_NAME = 'vulnerbilityfix'  # Replace with the branch name

headers = {
    'PRIVATE-TOKEN': PRIVATE_TOKEN

}

job_names = ['code_quality']  # Replace with the names of the jobs you want to trigger

for job_name in job_names:
    data = {
        'ref': BRANCH_NAME,
        'variables': {
            'CI_JOB_NAME': job_name,
        },
    }

    response = requests.post(f'{GITLAB_API_URL}/projects/{PROJECT_ID}/pipeline', json=data, headers=headers, verify=False)

    if response.status_code == 201:
        print(f'Job "{job_name}" triggered successfully')
    else:
        print(f'Failed to trigger job "{job_name}":', response.text)
# import requests

# # GitLab API variables
# GITLAB_URL = 'https://gitlab.os3.com/api/v4/'  # Update this to your GitLab instance URL
# PROJECT_ID = '100'  # Replace with your GitLab project's ID
# JOB_TOKEN = 'Fx1nwyyykeumx9TFgFmS'  # Replace with your job trigger token
# JOB_NAME = 'code_quality'  # Replace with the name of the job you want to trigger

# def trigger_job():
#     headers = {
#         'PRIVATE-TOKEN': JOB_TOKEN
#     }
    
#     # API endpoint to trigger a specific job
#     endpoint = f'{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/trigger/pipeline'
    
#     payload = {
#         'token': JOB_TOKEN,
#         'ref': 'vulnerbilityfix',  # Branch name where the job is defined
#         'variables[JOB_NAME]': 'true'  # Set a variable with the job name to trigger it
#     }
    
#     response = requests.post(endpoint, headers=headers, json=payload, verify=False)
    
#     if response.status_code == 201:
#         print(f'Job "{JOB_NAME}" triggered successfully!')
#     else:
#         print(f'Failed to trigger job. Status code: {response.status_code}')
#         print(response.text)

# if __name__ == '__main__':
#     trigger_job()
