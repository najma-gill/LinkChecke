import re
global_patterns = {
    'utm_source': re.compile(r"^[A-Za-z]{2,}$"),
    'utm_medium': re.compile(r'^[A-Za-z]{2,}$'),
    'utm_campaign': re.compile(r"^[A-Za-z0-9]+$"),
    'utm_content': re.compile(r'^[A-Za-z0-9]+$'),
    'utm_term': re.compile(r'^[A-Za-z0-9]+$'),
    'CH': re.compile(r'^[A-Z](-?[A-Z]){0,4}$'),
    'PR': re.compile(r'^[A-Z][a-zA-Z0-9-]*[a-zA-Z0-9]$'),
    'FL': re.compile(r'^0\d'),
    'DE': re.compile(r'^[A-Z][a-zA-Z]*$'),
    'KZ': re.compile(r'^[A-Za-z]+\-?[A-Za-z]+$'),
    'TI': re.compile(r'^[A-Z][a-zA-Z0-9-]*[a-zA-Z0-9]$'),
    'LA': re.compile(r'^([A-Z]{2}|BR-FR|BE-NL|CH-DE|CH-FR|CH-IT)$'),
    'ID': re.compile(r'^\d{3,}$'),
    'TM': re.compile(r'^[A-Z][a-zA-Z0-9-]*[a-zA-Z0-9]$'),
    'TP': re.compile(r'^(Par|NotP|Unkn)$'),
    'V': re.compile(r'^\d{2,}$'),
    'TR': re.compile(r'^[a-zA-Z]+\d*[a-zA-Z0-9-]*$'),
    'TG': re.compile(r'^(Male|Fem|FemUnkn|MF|Unkn)$'),
    'NW': re.compile(r'^[A-Z][a-zA-Z0-9-]*[a-zA-Z0-9]$'),
    'TA': re.compile(r'^\d+[a-zA-Z-]*\d+[a-zA-Z]*$'),
    'FO': re.compile(r'^\d+[Xx]\d$'),
    'GS': re.compile(r'^(ConvMax|CPC|CPA|CPCV|eCPC|maxCPA|maxCPM|maxCPPI|maxROAS|tROAS|niedKost)$'),
    'OS': re.compile(r'^((A|a)nd(roid)?|(i|I)(OS|os))$'),
    'ST': re.compile(r'^[A-Z][a-zA-Z]+$'),
    'CR': re.compile(r'^[a-zA-Z]+$'),
    'CUA': re.compile(r'^[A-Z][a-zA-Z-][a-zA-Z]*$'),
    'C': re.compile(r'^[a-zA-Z0-9]+-?[a-zA-Z]+$'),
}

global_messages = {
    "utm_campaign": "utm_campaign ",
    "utm_medium": "utm_medium ",
    "utm_source": "utm_source ",
    "utm_content": "utm_content ",
    "utm_term": "utm_term ",
    "duplicate_key": " duplicate key",
    "equal_missing":" = sign is missing",
    "pipe_missing":" | sign is missing",
    "value_missing": " value is missing",
    "ampersand_missing":" & sign is missing",
    "underscore_missing":"_ sign is missing",
    "pattern_mismatch": " pattern mismatch",
    "empty_string": " is empty",
    "missing_pipe_at_end": " missing pipe sign at end of string",
    "missing": " is missing",
    "key_not_allowed": " is not allowed",
    "reserved_characters_are_not_allowed": " special characters are not allowed",

}