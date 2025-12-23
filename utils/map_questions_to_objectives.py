import json
from .build_prompt import build_prompt
from core.ai_client import OpenRouterClient



def map_questions_to_objectives(
    questions: list[str],
    curriculum: dict,
) -> dict:
    """
    Sends a single batched request to the LLM to map questions to objectives.
    """

    prompt = build_prompt(questions, curriculum)

    client = OpenRouterClient()
    raw_response = client.chat(prompt)
    content = raw_response["choices"][0]["message"]["content"]

    try:
        mapping = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError("AI returned invalid JSON")

    return mapping
