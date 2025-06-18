description: >
  This project uses GitHub Actions to automatically build a Docker image
  whenever specific files or directories are pushed to the repository.

  The Docker image includes:
    - A machine learning model (trained during the GitHub Actions workflow)
    - A data formatting pipeline
    - A Streamlit-based web application

environment_variables:
  DOCKER_USERNAME:
    description: >
      Your Docker Hub username. Used to authenticate and push the Docker image
      during the GitHub Actions workflow.
    required: true
    example: "your-docker-username"

  DOCKER_PASSWORD:
    description: >
      Your Docker Hub password or access token. Used alongside DOCKER_USERNAME
      to authenticate in the GitHub Actions workflow.
    required: true
    example: "your-docker-password-or-token"

