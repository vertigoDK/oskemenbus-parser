# Oskemen Bus Parser

A REST API service for fetching and parsing public transportation schedules for Oskemen (Ust-Kamenogorsk) city.

## Features

- Search for locations in Oskemen
- Get real-time bus schedules for any stop in the city
- Format schedule data in a user-friendly way

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Requests

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd oskemenbus-parser
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If requirements.txt is missing, install the required packages manually:

```bash
pip install fastapi uvicorn requests pydantic
```

## Running the Application

To start the server:

```bash
python main.py
```

This will start the server on http://0.0.0.0:8000

### Changing the Port

If you need to run the server on a different port, modify the port parameter in `main.py`:

```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Change 8000 to your desired port
```

## API Usage

### Get Bus Schedule

**Endpoint:** `POST /api/bus/schedule`

**Request Body:**
```json
{
  "stop_id": "17409"
}
```

**Response:**
```json
{
  "stop_id": "17409",
  "routes": [
    {
      "number": "1",
      "end_stop": "Защита",
      "arrival_times": ["через 4 минуты", "через 22 минуты"]
    },
    {
      "number": "42",
      "end_stop": "Н.Ахмирово",
      "arrival_times": ["на остановке", "через 16 минут"]
    }
  ]
}
```

## API Documentation

Once the server is running, visit:
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

