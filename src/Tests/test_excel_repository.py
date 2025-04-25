import pytest

from src.Core.ExcelRepository import ExcelRepository

def test_excel_repository_can_instantiate():
    try:
        database = ExcelRepository()
    except Exception as e:
        pytest.fail(f"instantiate fail: {e}")
    else:
        assert isinstance(database, ExcelRepository)

def test_excel_repository_have_sheets():
    database = ExcelRepository()
    assert isinstance(database.sheets, dict)

def test_can_add_sheet():
    database = ExcelRepository()
    assert database.add_sheet("test", "APTO")

def test_can_delete_sheet():
    database = ExcelRepository()
    assert database.delete_sheet("APTO TEST")