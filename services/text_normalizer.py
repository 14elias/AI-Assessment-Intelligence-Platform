import re

HEADER_FOOTER_PATTERNS = [
    r'Addis Ababa University',
    r'Civic.*Ethical.*Education',
    r'Final Exam',
    r'Regular Program',
    r'Exam\.? Date',
    r'Name[_\s]+ID',
    r'Faculty[_\s]+Department',
    r'Second Semester'
    r'\d+ Academic Year'
]

ANSWER_SHEET_PATTERN = r'\n\s*\d+\.\s*_{2,}.*'


def fix_spacing(text: str) -> str:
    # letterLower + letterUpper → space
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    # letter + digit
    text = re.sub(r'([A-Za-z])(\d)', r'\1 \2', text)
    text = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)

    # collapse multiple spaces
    text = re.sub(r'\s{2,}', ' ', text)
    return text


def remove_headers_and_footers(text: str) -> str:
    lines = text.splitlines()
    cleaned = []

    for line in lines:
        skip = False
        for pattern in HEADER_FOOTER_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                skip = True
                break
        if not skip:
            cleaned.append(line)

    text = "\n".join(cleaned)
    text = re.sub(ANSWER_SHEET_PATTERN, '', text)
    return text


def normalize_newlines(text: str) -> str:
    # Ensure each option starts on its own line
    text = re.sub(r'\s*([A-E])\.', r'\n\1.', text)

    # Ensure each question starts on new line
    text = re.sub(r'\s*(\d+)\.', r'\n\1.', text)

    # Collapse excessive newlines
    text = re.sub(r'\n{2,}', '\n', text)

    return text.strip()


def normalize_text(raw_text: str) -> str:
    text = fix_spacing(raw_text)
    text = remove_headers_and_footers(text)
    text = normalize_newlines(text)
    return text
