from fastapi import FastAPI, HTTPException

from database import person_database
from models import Person

app = FastAPI(
    title="Person API",
    description="A simple REST API for managing Person resources. Python equivalent of the Java EE 7 sample.",
    version="1.0.0",
)


@app.get("/resources/persons", response_model=list[Person])
def get_all_persons():
    """
    Get all persons from the database.
    Equivalent to PersonResource.get() in Java.
    """
    return person_database.current_list()


@app.get("/resources/persons/{person_id}", response_model=Person)
def get_person(person_id: int):
    """
    Get a specific person by their ID.
    Equivalent to PersonResource.get(int id) in Java.
    """
    person = person_database.get_person(person_id)
    if person is None:
        raise HTTPException(
            status_code=404,
            detail=f'Person with id "{person_id}" not found.',
        )
    return person


@app.get("/")
def root():
    """Root endpoint with API information."""
    return {
        "message": "Person API - Python FastAPI equivalent of Java EE 7 sample",
        "endpoints": {
            "all_persons": "/resources/persons",
            "person_by_id": "/resources/persons/{id}",
            "docs": "/docs",
        },
    }
