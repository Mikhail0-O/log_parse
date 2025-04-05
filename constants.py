import re

PATTERN = re.compile(
    r'(?P<log_level>DEBUG|INFO|WARNING|ERROR|CRITICAL) django.request: '
    r'(\w+|Internal Server Error:) (?P<handler>/[\w/]+)'
)
"""Шаблон для поиска совпадений по hadler и log_level."""
LOG_LEVELS = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
"""Уровни логирования."""
COL_WIDTHS = [8, 8, 8, 8, 8]
"""Отступы между колонками."""
