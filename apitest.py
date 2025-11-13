"""
Ejercicio práctico - Clase 12: Automatización de APIs (Parte 2)

E2E test: lifecycle completo de POST en JSONPlaceholder
Criterios:
 - Crear POST con datos aleatorios -> 201 + id
 - Actualizar título con PATCH -> 200 y título cambiado
 - Eliminar POST -> 200
 - Flujo completo en < 3s

Ejecutar: pytest -q --html=report.html

"""
import time
import uuid
import requests
import pytest

BASE = "https://jsonplaceholder.typicode.com"

@pytest.mark.e2e
def test_post_create_update_delete_lifecycle():
    start = time.perf_counter()

    # --- 1) CREATE ---
    payload = {
        "title": f"test-title-{uuid.uuid4()}",
        "body": f"test-body-{uuid.uuid4()}",
        "userId": 1
    }

    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 201, f"Expected 201 on create, got {r.status_code} - {r.text}"

    body = r.json()
    assert "id" in body, "Create response must include 'id'"
    post_id = body["id"]

    # --- 2) UPDATE (PATCH) ---
    new_title = "Título actualizado por PATCH"
    patch_r = requests.patch(f"{BASE}/posts/{post_id}", json={"title": new_title})
    assert patch_r.status_code == 200, f"Expected 200 on patch, got {patch_r.status_code} - {patch_r.text}"

    patched = patch_r.json()
    # JSONPlaceholder returns the patched resource in the response body
    assert patched.get("title") == new_title, f"Title was not updated in PATCH response: {patched}"

    # --- 3) DELETE ---
    del_r = requests.delete(f"{BASE}/posts/{post_id}")
    assert del_r.status_code == 200, f"Expected 200 on delete, got {del_r.status_code} - {del_r.text}"

    # --- 4) PERFORMANCE ---
    elapsed = time.perf_counter() - start
    assert elapsed < 3.0, f"End-to-end flow took too long: {elapsed:.3f}s (must be < 3s)"

    # Optional: small sanity print for CI logs
    print(f"E2E post lifecycle completed: id={post_id} elapsed={elapsed:.3f}s")
