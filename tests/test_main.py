import pytest
from httpx import AsyncClient
import sys
import os
# Añade el directorio src al path. 
#agrega el directorio src al sys.path dinámicamente, permitiendo 
# que el archivo test_main.py encuentre el módulo main dentro de src


from src.main import app  #importación de fastapi

@pytest.mark.asyncio
async def test_create_holiday():
    # Suponiendo que tu API tiene un endpoint POST '/holidays'
    payload = {
        "name": "Día de la Independencia",
        "date": "2025-09-18"
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/holidays/", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == payload["name"]
    assert response.json()["date"] == payload["date"]

@pytest.mark.asyncio
async def test_get_holiday():
    # Primero, crea un feriado
    payload = {
        "name": "Día del Trabajo",
        "date": "2025-05-01"
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Crear un feriado
        create_response = await client.post("/holidays/", json=payload)
        holiday_id = create_response.json()["id"]
        
        # Obtener el feriado creado
        response = await client.get(f"/holidays/{holiday_id}")
    
    assert response.status_code == 200
    assert response.json()["name"] == payload["name"]
    assert response.json()["date"] == payload["date"]

@pytest.mark.asyncio
async def test_update_holiday():
    # Crear un feriado
    payload = {
        "name": "Día de la Madre",
        "date": "2025-05-10"
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        create_response = await client.post("/holidays/", json=payload)
        holiday_id = create_response.json()["id"]

        # Actualizar el feriado
        updated_payload = {
            "name": "Día de la Madre Actualizado",
            "date": "2025-05-10"
        }
        response = await client.put(f"/holidays/{holiday_id}", json=updated_payload)
    
    assert response.status_code == 200
    assert response.json()["name"] == updated_payload["name"]

@pytest.mark.asyncio
async def test_delete_holiday():
    # Crear un feriado
    payload = {
        "name": "Navidad",
        "date": "2025-12-25"
    }
    async with AsyncClient(app=app, base_url="http://test") as client:
        create_response = await client.post("/holidays/", json=payload)
        holiday_id = create_response.json()["id"]

        # Eliminar el feriado
        response = await client.delete(f"/holidays/{holiday_id}")
    
    assert response.status_code == 204  # No content
