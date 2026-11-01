\# PSUSphere - Docker Deployment



\## Project Description



PSUSphere is a Django-based web application. This project containerizes the existing application using Docker so it can be built and run consistently on different computers.



\## Requirements



\- Docker Desktop

\- Docker Compose



\## Run the Project (Developer)



1\. Clone or download this repository.

2\. Open a terminal in the project root folder.

3\. Build the Docker image and start the application:



&#x20;  ```powershell

&#x20;  docker compose up --build

&#x20;  ```



4\. Open the application in your browser:



&#x20;  http://127.0.0.1:8000/



5\. To stop the application, press `Ctrl + C`, then run:



&#x20;  ```powershell

&#x20;  docker compose down

&#x20;  ```



\## Run the Project (Client)



The client configuration is inside the `for\_client` folder.



1\. Make sure Docker Desktop is running.

2\. Open a terminal inside the `for\_client` folder.

3\. Pull the image from Docker Hub:



&#x20;  ```powershell

&#x20;  docker compose pull

&#x20;  ```



4\. Start the application:



&#x20;  ```powershell

&#x20;  docker compose up

&#x20;  ```



5\. Open:



&#x20;  http://127.0.0.1:8000/



6\. To stop the application, press `Ctrl + C`, then run:



&#x20;  ```powershell

&#x20;  docker compose down

&#x20;  ```



\## Docker Hub Image



\[PSUSphere on Docker Hub](https://hub.docker.com/r/reynaldzxc/psusphere)



Image name:



`reynaldzxc/psusphere:latest`



\## Initial Account Setup



The Docker deployment uses a fresh database. Existing accounts and database records from the original development environment are not included.



To create an administrator account, open another terminal while the container is running and execute:



```powershell

docker compose exec web python manage.py createsuperuser

```



Follow the prompts to create a username and password.



\## Project Files



\- `Dockerfile` - Defines how the Docker image is built.

\- `docker-compose.yml` - Builds and runs the application.

\- `requirements.txt` - Lists the Python dependencies.

\- `.dockerignore` - Excludes unnecessary and private files from the Docker build.

\- `for\_client/docker-compose.yml` - Allows clients to pull and run the published Docker Hub image.



\## Notes



\- The SQLite database is not included in the Docker image.

\- Database migrations run automatically when the container starts.

\- A new administrator account must be created for a fresh deployment.

