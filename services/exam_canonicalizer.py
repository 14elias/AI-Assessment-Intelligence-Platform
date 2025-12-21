import re


QUESTION_PATTERN = re.compile(r'\n(\d+)\.\s*')


def canonicalize(text: str) -> str:
    # Convert numbered questions → Q<number>:
    text = QUESTION_PATTERN.sub(r'\nQ\1:\n', text)

    # Normalize options
    text = re.sub(r'\n([A-E])\.\s*', r'\n\1) ', text)

    # Remove stray page numbers (standalone digits)
    text = re.sub(r'\n\d+\n', '\n', text)

    # Trim whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{2,}', '\n', text)

    return text.strip()
