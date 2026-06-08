BLOCKED_PATTERNS = [

    "ignore previous instructions",

    "system prompt",

    "developer prompt",

    "reveal prompt"
]


def validate_query(query):

    query = query.lower()

    for pattern in BLOCKED_PATTERNS:

        if pattern in query:

            return False

    return True