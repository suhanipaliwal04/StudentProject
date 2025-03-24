# StudentProject
Project Description: StudentProject
StudentProject is a multi-app Django web application designed to be containerized using Docker and automated with Jenkins. The project consists of two Django apps (app1 and app2) with static views and templates for demonstration purposes.

Key Features:
Multi-App Django Structure:
app1 contains the homepage and about page with navigation links.
app2 includes a services and contact page.
No Database Usage: The project relies on static views and templates only.
Dockerized Deployment:
A Dockerfile is included to containerize the project.
The image is built using Python base image and runs the Django development server inside a container.
CI/CD Pipeline with Jenkins:
A Jenkinsfile automates the process of pulling the GitHub repository, building the Docker image, and pushing it to Docker Hub.
Docker Hub Integration:
The final Docker image is pushed to Docker Hub for easy access and deployment.
Deliverables:
GitHub Repository: Contains the full source code, Dockerfile, and Jenkinsfile.
Docker Hub Image: A publicly accessible Docker image of the project.
README File: Provides instructions for setting up and running the project.
