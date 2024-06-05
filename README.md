# P1 Django Take-Home Assignment

## Problem Statement: World Needs More Food Trucks

### About

* A minimum viable product built as part of the take-home assignment.

* Developed using Django and Django REST Framework (DRF).

### Setup

* Create a virtual environment using `python -m venv venv/`.

* Activate the virtual environment using `venv\Scripts\activate.bat` on Windows, or `venv/bin/activate` on Linux.

* Install the required dependencies using `pip install -r requirements.txt`

* Copy the contents of `.env.template` to `.env` using `copy .env.template .env` in the terminal, or simply rename `.env.template` to `.env`.

* Once all the dependencies have been installed, `cd` into the `food_truck` directory and run `python manage.py migrate`.

### Loading the data from the CSV file into the database

* To help with rapid prototyping, I chose SQLite as the database. Since it is lightweight and file-based, so quick iterations and repeated migrations are painless.

* A helper script `importer.py` was created to quickly load the data in the `food-truck-data.csv` file into the database using `pandas`. Run it using `python importer.py`

* All the data will have been loaded into the table.

### Firing up the server

* Run the server using `python manage.py runserver` and navigate to [http:localhost:8000](http://localhost:8000).

* There are 2 endpoints available:

  * /trucks - A GET request to this endpoint returns **all** the food trucks present in the database, that have a facility type of `Truck` and have a permit that is either in the `Issued` or `Approved` state (we don't want to show the user food trucks/restaurants with expired or suspended permits).

  * /find - A POST request with two required parameters (`latitude` and `longitude`, of type floating-point) to this endpoint returns the 10 food trucks that are closest to the coordinates provided. Again, only those establishments that have a facility type of `Truck` and active permits are shown.
  