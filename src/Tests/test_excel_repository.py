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

def test_can_edit_sheet():
    database = ExcelRepository()

    database.add_sheet("test 1", "APTO")
    result = database.edit_sheet("APTO TEST 1", "TEST 2", "APTO")
    database.delete_sheet("APTO TEST 2")
    
    assert result

def test_can_edit_without_type():
    database = ExcelRepository()

    database.add_sheet("test 2", "APTO")
    result = database.edit_sheet("APTO TEST 2", "TEST 3", None)
    database.delete_sheet("APTO TEST 3")
    
    assert result

def test_can_edit_without_new_name():
    database = ExcelRepository()

    database.add_sheet("test 3", "APTO")
    result = database.edit_sheet("APTO TEST 3", None, "APTO")
    database.delete_sheet("APTO TEST 3")
    
    assert result