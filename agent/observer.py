def observe_result(result):
    if result is None:
        return {
            "status": "failed",
            "error": "Tool returned no result"
        }

    if isinstance(result, list) and len(result) == 0:
        return {
            "status": "failed",
            "error": "Tool returned empty results"
        }

    return {
        "status": "success",
        "message": "Workflow step completed successfully"
    }