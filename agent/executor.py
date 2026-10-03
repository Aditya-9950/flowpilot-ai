
from agent.planner import generate_workflow
from tools.search import search_web, alternate_search
from agent.observer import observe_result
from agent.repair import repair_workflow


def execute_workflow(goal: str):
    logs = []

    def log(stage, message, status="info"):
        event = {
            "stage": stage,
            "message": message,
            "status": status,
        }
        logs.append(event)
        print(f"[{stage}] {message}")

    # -----------------------------
    # 1. PLANNING
    # -----------------------------
    log("PLANNER", "Creating workflow...")

    workflow = generate_workflow(goal)

    log(
        "PLANNER",
        "Workflow generated successfully.",
        "success",
    )

    # -----------------------------
    # 2. EXECUTION
    # -----------------------------
    log("EXECUTOR", "Starting primary tool...")

    try:
        result = search_web(goal)

        log(
            "EXECUTOR",
            "Primary tool completed successfully.",
            "success",
        )

    except Exception as error:

        log(
            "EXECUTOR",
            f"Primary tool failed: {error}",
            "error",
        )

        # -----------------------------
        # 3. AI REPAIR
        # -----------------------------
        log(
            "REPAIR AGENT",
            "Analyzing failure with Qwen3...",
        )

        repair = repair_workflow(str(error))

        log(
            "REPAIR AGENT",
            f"AI decision: {repair['action']}",
            "success",
        )

        # -----------------------------
        # 4. FALLBACK
        # -----------------------------
        log(
            "EXECUTOR",
            "Applying recovery strategy...",
        )

        result = alternate_search(goal)

        log(
            "EXECUTOR",
            "Fallback tool completed successfully.",
            "success",
        )

    # -----------------------------
    # 5. OBSERVATION
    # -----------------------------
    log(
        "OBSERVER",
        "Verifying workflow result...",
    )

    observation = observe_result(result)

    if observation["status"] == "success":

        log(
            "OBSERVER",
            "Result verified successfully.",
            "success",
        )

        log(
            "FLOWPILOT",
            "Workflow completed and recovered successfully.",
            "success",
        )

    else:

        log(
            "OBSERVER",
            "Result verification failed.",
            "error",
        )

    return {
        "workflow": workflow,
        "result": result,
        "observation": observation,
        "logs": logs,
    }
