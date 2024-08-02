"# fitphysique-backend" 

This is the backend server for the FitPhysique project, built with Django.

## Installation

1. Clone the repository:
git clone https://github.com/Ashutosh2ingh/fitphysique-backend.git


2. Set up a virtual environment (recommended):
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt


4. Apply migrations:
python manage.py migrate


## Usage

To start the development server:
python manage.py runserver


## Configuration

Ensure you have a `.env` file set up with necessary environment variables.

## Contributing

1. Fork the repository and create your branch from `main`.
2. Pull requests are welcome. Please make sure to update tests as appropriate.

## Note

- The `sqlite3` database file (`db.sqlite3`) and virtual environment (`venv/`) are included in `.gitignore` and should not be pushed to the repository.
