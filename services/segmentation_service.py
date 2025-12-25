import re
from typing import List, Tuple
from .schema import Question, RejectedQuestion


QUESTION_SPLIT_PATTERN = re.compile(r'Q(\d+):')

MAX_JUMP = 5  

def sanitize_question_number(
    raw_number: int,
    expected_number: int
) -> int:
    """
    Fix broken question numbers caused by page numbers or OCR noise.
    """
    if raw_number == expected_number:
        return raw_number

    if raw_number == expected_number + 1:
        return raw_number

    # Suspicious large jump (e.g. 41 -> 642)
    if raw_number > expected_number + MAX_JUMP:
        return expected_number

    # Backward numbering or duplicates
    if raw_number < expected_number:
        return expected_number

    return raw_number


def remove_trailing_noise(text: str) -> str:
    # Remove exam metadata
    text = re.sub(
        r'(Exam\.?\s*Date.*|Name[_\s]*.*|Second Semester.*)',
        '',
        text,
        flags=re.IGNORECASE
    )

    # Remove trailing standalone numbers
    text = re.sub(r'\s+\d{1,3}$', '', text)

    return text.strip()




def segment_questions(text: str):
    parts = QUESTION_SPLIT_PATTERN.split(text)[1:]

    questions = []
    rejected = []

    expected_number = 1

    for i in range(0, len(parts), 2):
        raw_number = int(parts[i])
        block = parts[i + 1].strip()

        number = sanitize_question_number(raw_number, expected_number)

        try:
            question_text, options = parse_block(block)

            question_text = remove_trailing_noise(question_text)

            if len(options) < 2:
                raise ValueError("Less than 4 options")

            questions.append(
                Question(
                    number=number,
                    text=question_text,
                    options=options
                )
            )

            expected_number = number + 1

        except Exception as e:
            rejected.append(
                RejectedQuestion(
                    raw_block=f"Q{raw_number}:\n{block}",
                    reason=str(e)
                )
            )

    return questions, rejected



def parse_block(block: str) -> tuple[str, list[str]]:
    lines = block.splitlines()

    question_lines = []
    options = []

    for line in lines:
        if re.match(r'[A-E]\)', line):
            options.append(line[2:].strip())
        else:
            question_lines.append(line.strip())

    question_text = ' '.join(question_lines).strip()

    if not question_text:
        raise ValueError("Empty question text")

    return question_text, options
