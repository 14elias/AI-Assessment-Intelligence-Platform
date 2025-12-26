import json
import re
from .build_prompt import build_prompt
from core.ai_client import OpenRouterClient



async def map_questions_to_objectives(
    questions: list[str],
    curriculum: dict,
) -> dict:
    """
    Sends a single batched request to the LLM to map questions to objectives.
    """

    prompt = build_prompt(questions, curriculum)

    client = OpenRouterClient()
    raw_response = await client.chat(prompt)
    content = raw_response["choices"][0]["message"]["content"]
    print(content)

    if not content or not content.strip():
        raise ValueError("AI returned empty response")

    content = content.strip()

    # Remove markdown code fences if present
    if content.startswith("```"):
        content = content.split("```")[1].strip()
    
    match = re.search(r"\[\s*{.*}\s*\]", content, re.DOTALL)
    if not match:
        raise ValueError(f"No valid JSON found:\n{content}")
    
    try:
        mapping = json.loads(match.group())
    except json.JSONDecodeError:
        raise ValueError("AI returned invalid JSON")

    return mapping
