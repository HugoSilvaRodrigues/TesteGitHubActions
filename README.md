# Docker Project with GitHub Actions

This project uses GitHub Actions to automatically build a Docker image whenever specific files or directories are pushed to the repository.

## The Docker image includes:

- A machine learning model (trained during the GitHub Actions workflow)  
- A data formatting pipeline  
- A web application built with Streamlit  

---

## Environment Variables

For the workflow to run correctly, the following environment variables (GitHub Secrets) must be set:

| Variable          | Description                                                                                     | Required | Example                    |
|-------------------|-------------------------------------------------------------------------------------------------|----------|----------------------------|
| `DOCKER_USERNAME` | Your Docker Hub username. Used to authenticate and push the Docker image.                      | Yes      | `your-docker-username`      |
| `DOCKER_PASSWORD` | Your Docker Hub password or access token. Used together with the username for authentication.  | Yes      | `your-password-or-token`    |

> **Important:** These variables must be configured under **Settings > Secrets and variables > Actions** in GitHub. They **are not exposed in the code** and are kept secure.

