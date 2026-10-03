import ollama


def generate_workflow(goal: str) -> str:
    prompt = f"""
You are the planning engine of FlowPilot, an autonomous workflow automation agent.

User goal:
{goal}

Create a simple workflow for achieving this goal.

Return ONLY a numbered list of steps.
Each step should contain:
- action
- tool

Example:
1. Search for relevant information using web_search
2. Analyze the results using llm
3. Create a final report using llm
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

    return response["message"]["content"]