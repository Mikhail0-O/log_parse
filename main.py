import argparse
import re
from collections import defaultdict

from constants import PATTERN, LOG_LEVELS, COL_WIDTHS


def parse_files(files: list[str]) -> tuple[defaultdict, int]:
    handler_counter: defaultdict = defaultdict(
        lambda: {level: 0 for level in LOG_LEVELS}
    )
    total_requests: int = 0
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    match = re.search(PATTERN, line)
                    if match:
                        handler_counter[
                            match.group('handler')
                        ][match.group('log_level')] += 1
                        total_requests += 1
        except FileNotFoundError as error:
            print(f'Ошибка: файл {file} не найден', error)
    return handler_counter, total_requests


def get_row_handler_level_sorted(handler_counter: defaultdict) -> str:
    table: list[str] = []
    for handler, levels in sorted(handler_counter.items()):
        row = (
            f'{handler:<25}' + ''.join(
                f'{levels[lvl]:^{COL_WIDTHS[i]}}'
                for i, lvl in enumerate(LOG_LEVELS))
        )
        table.append(row)
    return '\n'.join(table)


def print_report(handler_counter: defaultdict, total_requests: int) -> None:
    header = (
        f'{"HANDLER":<25}' +
        ''.join(
            f'{lvl:^{width}}' for lvl, width in zip(LOG_LEVELS, COL_WIDTHS)
        )
    )
    print(f'\nTotal requests: {total_requests}')
    print(f'\n{header}\n{"-" * 65}')
    print(get_row_handler_level_sorted(handler_counter))
    total_row = [
        sum(levels[level] for levels in handler_counter.values())
        for level in LOG_LEVELS
    ]
    total_row_str = (
        f'{" ":<25}' +
        ''.join(f'{val:^{w}}' for val, w in zip(total_row, COL_WIDTHS))
    )
    print(f'{"-" * 65}\n{total_row_str}\n{"-" * 65}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Парсинг логов Django')
    parser.add_argument(
        'logs', nargs='+', help='Файлы логов'
    )
    parser.add_argument(
        '--report', choices=['handler'], required=True, help='Тип отчета'
    )
    args = parser.parse_args()
    handler_counter, total_requests = parse_files(args.logs)
    print_report(handler_counter, total_requests)


if __name__ == '__main__':
    main()
