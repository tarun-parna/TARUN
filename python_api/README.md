# Person API - Python FastAPI

This is a Python FastAPI equivalent of the Java EE 7 REST API sample.

## Overview

A simple REST API for managing Person resources, featuring characters from The Big Bang Theory.

## Installation

```bash
cd python_api
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint with API information |
| GET | `/resources/persons` | Get all persons |
| GET | `/resources/persons/{id}` | Get a specific person by ID |
| GET | `/docs` | Interactive API documentation (Swagger UI) |

## Sample Data

The API comes pre-loaded with the following persons:
- 0: Penny
- 1: Leonard
- 2: Sheldon
- 3: Amy
- 4: Howard
- 5: Bernadette
- 6: Raj
- 7: Priya

## Example Usage

```bash
# Get all persons
curl http://localhost:8000/resources/persons

# Get person by ID
curl http://localhost:8000/resources/persons/2
```
