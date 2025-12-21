import re



def normalize_newlines(text: str) -> str:
    # Ensure questions start on new lines
    text = re.sub(r"\s*(\d+)\.", r"\n\n\1.", text)

    # Ensure options start on new lines
    text = re.sub(r"\s*([A-E])\.", r"\n\1.", text)

    # Collapse excessive newlines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# def remove_noise(text: str) -> str:
#     patterns = [
#         r"Page\s+\d+",
#         r"Addis Ababa University.*",
#         r"©.*",
#         r"AlignEd University",
#         r"Course:\s*.*",
#     ]

#     for pattern in patterns:
#         text = re.sub(pattern, "", text, flags=re.IGNORECASE)

#     return text




def remove_instructions(text: str) -> str:

    INSTRUCTION_PATTERNS = [
        r"Part\s+One:.*?(?=\n\d+\.)",   # Part One instructions
        r"Choose the correct answer.*?(?=\n\d+\.)",
        r"Addis Ababa University.*",
        r"\dAddis Ababa University.*",
        r"Name\s*_+.*",
        r"I\.D\.No\..*",
        r"Exam\.?Date.*",
        r"Faculty.*",
        r"Department.*",
    ]

    for pattern in INSTRUCTION_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE | re.DOTALL)

    return text.strip()


def remove_marks(text: str) -> str:
    text = re.sub(r"\(\s*\d+\s*marks?\s*\)", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\[\s*\d+\s*marks?\s*\]", "", text, flags=re.IGNORECASE)
    return text


def remove_answer_sheet(text: str) -> str:
    return re.sub(r"\d+\.\s*_+", "", text)


def fix_broken_lines(text: str) -> str:
    lines = text.split("\n")
    fixed = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if fixed and not fixed[-1].endswith((".", "?", ":")):
            fixed[-1] += " " + line
        else:
            fixed.append(line)

    return "\n".join(fixed)



def remove_footer_lines(text: str) -> str:

    FOOTER_KEYWORDS = [
        "addis",
        "university",
        "civic",
        "ethic",
        "finalexam",
        "coordinatingunit",
        "regularprogram",
        "semester",
        "academicyear",
    ]

    cleaned_lines = []

    for line in text.splitlines():
        normalized = line.lower().replace(" ", "")

        if any(keyword in normalized for keyword in FOOTER_KEYWORDS):
            continue  # drop footer line

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)



def clean_text(raw_text: str) -> str:
    text = raw_text

    text = remove_instructions(text)
    text = remove_footer_lines(text)
    text = normalize_newlines(text)
    text = remove_marks(text)
    text = remove_answer_sheet(text)
    text = fix_broken_lines(text)

    return text
