import json
from core.ai_client import OpenRouterClient

async def extract_questions_with_ai(raw_text: str) -> dict:
    """
    Uses an LLM to extract exam questions from raw PDF text.

    Returns a dict with the structure:
    {
        "questions": [
            {
                "number": int,
                "text": str,
                "options": list[str] | null,
                "points": int | null
            }
        ]
    }
    """


    client = OpenRouterClient()

    prompt = f"""
You are given:

1) Raw text extracted from a PDF exam (may contain noise).
2) The text may include headers, footers, instructions, and page artifacts.

Your task:
- Extract ONLY the actual exam questions.
- Ignore all non-question content.

Extraction rules:
- REMOVE school names, dates, headers, footers, and page numbers.
- REMOVE general instructions (e.g., "Answer all questions", "Time allowed").
- KEEP the exact wording of each question.
- If a question has multiple-choice options, extract them as a list.
- If a question has no options, set "options" to null.
- If points/marks are mentioned, extract the number.
- If points are NOT mentioned, set "points" to null.
- Preserve the original question numbering if present.

Return ONLY valid JSON in the following format:

{{
  "questions": [
    {{
      "number": 1,
      "text": "Full question text",
      "options": ["Option A", "Option B", "Option C", "Option D"] | null,
      "points": 2 | null
    }}
  ]
}}

Raw exam text:
{raw_text}

Important rules:
- Respond with JSON only
- No explanations
- No markdown
- No extra text
"""


    try:
        raw_response = await client.chat(prompt)
        content = raw_response["choices"][0]["message"]["content"]
        if not content:
            raise ValueError("Empty response from AI")

        parsed = json.loads(content)

        if "questions" not in parsed or not isinstance(parsed["questions"], list):
            raise ValueError("Invalid JSON structure returned by AI")

        return parsed

    except json.JSONDecodeError as e:
        raise ValueError(f"AI returned invalid JSON: {e}") from e

    except Exception as e:
        raise RuntimeError(f"Failed to extract questions: {e}") from e
