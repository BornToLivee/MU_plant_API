# Plant watered API

Test task for Mobilunity company

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BornToLivee/MU_plant_API.git
   cd plant_watered_api
   ```
   
2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

## Usage

1. Run the development server:

   ```bash
   python manage.py runserver
   ```

2. Access the application at http://127.0.0.1:8000.


## API Endpoints

| Method | Endpoint            | Description              |
|--------|----------------------|--------------------------|
| GET    | `/api/plants/`      | List all plants         |
| POST   | `/api/plants/`      | Create a new plant      |
| GET    | `/api/plants/<id>/` | Retrieve a plant by ID  |
| PUT    | `/api/plants/<id>/` | Update a plant watered date by ID|
| GET   | `/api/plants/<id>/mark_watered/` | Set plant watered date on current date|


## Testing

To run tests:
   ```bash
   python manage.py test