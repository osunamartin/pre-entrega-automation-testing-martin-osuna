import pytest

test_files = [
    "tests/test_inventory.py",
    "tests/test_login_csv.py",
    "tests/test_api_reqres.py",
]

pytest_args = test_files + ["-v", "--html=report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)