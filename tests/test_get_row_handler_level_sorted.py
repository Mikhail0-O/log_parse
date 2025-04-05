from main import get_row_handler_level_sorted

from tests.conftest import UNSORTED_HANDLER_LEVEL, SORTED_HANDLER_LEVEL


def test_get_row_handler_level_sorted():
    """Проверяет сортировку строк в таблице."""
    handeler_level = get_row_handler_level_sorted(UNSORTED_HANDLER_LEVEL)
    assert handeler_level.strip() == SORTED_HANDLER_LEVEL.strip()
