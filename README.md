# Movie Cave

Movie Cave is a movie downloads and aggregation website for the African market.

## Design Requirements

- Lightweight MySQL database: The application uses a lightweight MySQL database to store user data efficiently.

- Movie Links: Instead of storing the actual movies, Movie Cave only contains links to web directories where these movies are stored. This approach allows for a more scalable and flexible solution.

- Flask Backend and Jinja Frontend: The backend of Movie Cave is built using Flask, a lightweight web framework in Python. The frontend is powered by Jinja, a templating engine that allows for dynamic content rendering. In the future, React will be integrated to enhance the user experience.

- Simple MySQL Database: Movie Cave utilizes a simple MySQL database to manage user data and movie links. This choice ensures ease of use and maintainability.

## Getting Started

To get started with Movie Cave, follow these steps:

1. Clone the repository:
```
git clone https://github.com/alemiherbert/movie-cave.git
```
2. Set up the virtual enable the virtualenvironment 
```
source ./.venv/bin/activate
```

3. Install the required dependencies: 
```
pip install -r requirements.txt
```

4. Set the environment variables
```
$ export FLASK_APP=app
$ export FLASK_DEBUG=true
$ flask run
``` 

5. Access Movie Cave in your web browser at `http://localhost:5000`



