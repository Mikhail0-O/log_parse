import pytest

from main import parse_files
from tests.conftest import (
    EXPECTED_HANDLER_LEVEL_1, EXPECTED_TOTAL_REQUESTS_1,
    EXPECTED_HANDLER_LEVEL_2, EXPECTED_TOTAL_REQUESTS_2,
    EXPECTED_HANDLER_LEVEL_3, EXPECTED_TOTAL_REQUESTS_3)


@pytest.mark.parametrize(
        'file, expected_handler_level, expected_total_requests',
        [
            (
                'tests/test_1.log', EXPECTED_HANDLER_LEVEL_1,
                EXPECTED_TOTAL_REQUESTS_1
            ),
            (
                'tests/test_2.log', EXPECTED_HANDLER_LEVEL_2,
                EXPECTED_TOTAL_REQUESTS_2
            ),
            (
                'tests/test_3.log', EXPECTED_HANDLER_LEVEL_3,
                EXPECTED_TOTAL_REQUESTS_3
            ),
        ]
)
def test_parse_files(file, expected_handler_level, expected_total_requests):
    """Проверяет подсчет уровней логирования."""
    handeler_level, total_requests = parse_files([file, ])
    assert len(handeler_level) == len(expected_handler_level)
    assert handeler_level == expected_handler_level
    assert total_requests == expected_total_requests
