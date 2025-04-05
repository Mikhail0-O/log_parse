# Django Log Parser

CLI-приложение для анализа логов Django и формирования табличного отчета по уровням логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL) с разбивкой по обработчикам (HANDLER).

# Стек

- Python 3.12
- Стандартные библиотеки (argparse, re, defaultdict)

# Установка 

Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/log_parse.git
cd log_parse
```

# Использование

Можно указать один файл для логов:

```bash
python main.py путь/к/логу.log --report handler
```

Можно указать сразу несколько файлов логов:

```bash
python main.py лог1.log лог2.log лог3.log --report handler
```

# Пример вывода

```bash

Total requests: 16727101

HANDLER                   DEBUG    INFO  WARNING  ERROR  CRITICAL
-----------------------------------------------------------------
/admin/dashboard/           0     760326    0     253442    0    
/admin/login/               0    1013765    0     506881    0    
/api/v1/auth/login/         0    1267204    0     253441    0    
/api/v1/cart/               0    1267203    0     253440    0    
/api/v1/checkout/           0    1013766    0     506881    0    
/api/v1/orders/             0    1013762    0     253442    0    
/api/v1/payments/           0     506887    0       1       0    
/api/v1/products/           0    1013763    0     506880    0    
/api/v1/reviews/            0    1774085    0     760320    0    
/api/v1/reviews_1/          0       1       0       0       0    
/api/v1/shipping/           0     760322    0     253441    0    
/api/v1/support/            0    1774081    0     253443    0    
/api/v1/users/              0     506884    0     253440    0    
-----------------------------------------------------------------
                            0    12672049   0    4055052    0    
-----------------------------------------------------------------
```