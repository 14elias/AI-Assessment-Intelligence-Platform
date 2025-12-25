from . import format_question

def build_prompt(questions: list[str], curriculum: dict) -> str:
    """
    Builds a strict prompt for mapping exam questions to curriculum objectives.
    """

    # Flatten objectives into a readable list
    objective_lines = []
    for topic in curriculum.course.topics:
        for obj in topic.objectives:
            objective_lines.append(
                f'{obj.id}: {obj.description}'
            )

    objectives_text = "\n".join(objective_lines)

    questions_text = questions

    prompt = f"""
You are given:

1) A list of exam questions (some are multiple-choice).
2) A curriculum consisting of topics and learning objectives.

Your task:
- For EACH question, determine the MOST RELEVANT learning objective(s).
- A question may map to MORE THAN ONE objective if appropriate.
- Do NOT invent objectives.
- If no objective matches, return an empty list.

Return ONLY valid JSON in the following format:

[
  {{
    "question_number": 1,
    "objective_ids": [3, 5],
    "confidence": 0.82
  }}
]

Questions:
{questions_text}

objectives:
{objectives_text}

Important rules:
- Respond with JSON only
- No explanations
- No markdown
"""

    return prompt
