UNSORTED_HANDLER_LEVEL = {
    '/api/v1/reviews/': {
        "DEBUG": 0, "INFO": 1, "WARNING": 0, "ERROR": 0, "CRITICAL": 0
    },
    '/api/v1/orders_by/': {
        "DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 1, "CRITICAL": 0
    },
    '/api/v1/users/123/': {
        "DEBUG": 1, "INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0
    },
}
SORTED_HANDLER_LEVEL = (
    '/api/v1/orders_by/          0       0       0       1       0    \n'
    '/api/v1/reviews/            0       1       0       0       0    \n'
    '/api/v1/users/123/          1       0       0       0       0    \n'
)
EXPECTED_HANDLER_LEVEL_1 = {
    '/api/v1/reviews/': {
        "DEBUG": 0, "INFO": 1, "WARNING": 0, "ERROR": 0, "CRITICAL": 0
    },
    '/api/v1/orders_by/': {
        "DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 1, "CRITICAL": 0
    },
    '/api/v1/users/123/': {
        "DEBUG": 1, "INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0
    },
}
EXPECTED_HANDLER_LEVEL_2 = {
    '/api/v1/reviews/': {
        "DEBUG": 0, "INFO": 1, "WARNING": 0, "ERROR": 0, "CRITICAL": 0
    },
    '/api/v1/orders/': {
        "DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 1, "CRITICAL": 0
    },
    '/api/v1/users/123/': {
        "DEBUG": 1, "INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0
    },
}
EXPECTED_HANDLER_LEVEL_3 = {
    '/api/v1/reviews/': {
        "DEBUG": 0, "INFO": 1, "WARNING": 0, "ERROR": 0, "CRITICAL": 0
    },
    '/api/v1/orders_by/': {
        "DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 1, "CRITICAL": 0
    },
    '/api/v1/auth/login/': {
        "DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 2, "CRITICAL": 0
    },
}
EXPECTED_TOTAL_REQUESTS_1 = 3
EXPECTED_TOTAL_REQUESTS_2 = 3
EXPECTED_TOTAL_REQUESTS_3 = 4
