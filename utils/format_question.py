def format_mcq_question(q) -> str:
    lines = [f"Q{q.number}. {q.text.strip()}", ""]

    option_labels = ["A", "B", "C", "D", "E", "F"]
    for label, option in zip(option_labels, q.options or []):
        lines.append(f"{label}. {option.strip()}")

    return "\n".join(lines)
