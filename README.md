# Trivia App

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game.

## Getting Started

### Setting up the Backend

### Installing Dependencies

> The system used here is windows 10

1. **Python** - Follow instructions to install the latest version of python for your platform in the [python download](https://www.python.org/downloads/)

2. **Virtual Environment** - It is recommended to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
psql -U postgres
```

and

```bash
CREATE DATABASE trivia;
```

> postgres is the postgresql user

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql -U posrgres trivia < trivia.psql
```

### Run the Server

From within the `./backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run --reload
```

### Testing

To deploy the tests, run

```bash
psql -U postgres
```

and

```bash
CREATE DATABASE trivia_test;
```

```bash
psql -U posrgres trivia_test < trivia.psql
py test_flaskr.py
```

### Setting up the Frontend

The [frontend](./frontend) is created using React frontend to consume the data from the Flask server which is located in the [Backend](./backend).

### Installing Dependencies

1. **Installing Node and NPM**
   This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

2. **Installing project dependencies**
   This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _tip_: `npm i` is shorthand for `npm install``

### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

```bash
npm start
```

## API Reference

> The API can be found in [Backend](./backend) directory.

## Authors

- Udacity Team
- Oluwatimilehin Idowu

## Acknowledgements

I would like to acknowledge the contributions of the Udacity Team, the session leads, career coaches, and all my fellow learners.
