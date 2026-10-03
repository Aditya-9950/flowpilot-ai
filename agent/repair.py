import ollama


def repair_workflow(error: str):
    print("\n[REPAIR AGENT] Analyzing failure...")

    prompt = f"""
You are the repair agent of FlowPilot.

A workflow tool has failed.

Error:
{error}

Available repair actions:
1. retry
2. use_fallback

Choose the most appropriate action.

Return ONLY one of:
retry
use_fallback
"""

    response = ollama.chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    decision = response["message"]["content"].strip().lower()

    print(f"[REPAIR AGENT] AI decision: {decision}")

    if "use_fallback" in decision:
        return {
            "action": "use_fallback",
            "reason": "AI selected fallback after analyzing the failure"
        }

    return {
        "action": "retry",
        "reason": "AI selected retry"
    }