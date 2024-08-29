import subprocess
import os
import json

def read_project_json(file_path):
    
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def build_and_push_image(dockerfile_path, image_tag, context_dir):
    
    try:
        print(f"Building Docker image {image_tag}...")
        subprocess.run([
            'docker', 'build', '-f', dockerfile_path,'-t', f"{image_tag}", context_dir
        ], check=True)

        print(f"Pushing Docker image {image_tag}...")
        subprocess.run([
            'docker', 'push', f"{image_tag}"
        ], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        raise

def main():
    
    # Replace below line of code to fetch Widget uploaded and it's Code Path
    # Also fetch other required fields from Pakckage.json file
    
    dockerhub_path = "nitinsuvagia" # we will create "quantumdatalytica"
    folders = ['ChoiceFetchReportsMachine', 'InitWorkflowMachine','PasswordLockerMachine']  # Replace with your folders using Parameters
    run_path = "../QuantamDataLytics-POC/Machine"

    for folder in folders:

        dockerfile_path = os.path.join(run_path, folder, 'Dockerfile')
        context_dir = os.path.join(run_path,folder)    # It's current Directory of Dockerfile
        projectfile_path = os.path.join(context_dir,"Project.json")

        projectJson = read_project_json(projectfile_path)
        
        image_name = projectJson.get("name").lower().replace(" ","")
        version = projectJson.get("version")
        image_tag = f"{dockerhub_path}/{image_name}:{version}"

        build_and_push_image(dockerfile_path, image_tag, context_dir)

if __name__ == "__main__":
    main()
