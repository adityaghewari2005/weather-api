Dockerized Weather API | Python, Flask, Docker, Docker Compose

Developed a RESTful Weather API using Python Flask and containerized the application using Docker. Configured Docker Compose for container management and implemented health-check endpoints and basic container monitoring using Docker Stats and Logs.



             GitHub
                │
                ↓
        ┌───────────────┐
        │ Docker Image  │
        │ weather-api   │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │   Container   │
        │ Python Flask  │
        └───────┬───────┘
                ↓
       localhost:5000
          ↙     ↓     ↘
       /      /weather  /health
                │
                ↓
          Docker Stats
          Docker Logs
