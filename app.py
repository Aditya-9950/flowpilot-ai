import streamlit as st
from agent.executor import execute_workflow


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="FlowPilot | Autonomous AI",
    page_icon="✈️",
    layout="wide",
)


# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .hero {
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(135deg, #111827, #312e81);
        color: white;
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #d1d5db;
        margin-top: 6px;
    }

    .metric-card {
        padding: 20px;
        background: white;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        text-align: center;
    }

    .metric-label {
        font-size: 13px;
        color: #6b7280;
    }

    .metric-value {
        font-size: 25px;
        font-weight: 800;
    }

    .event {
        padding: 16px 20px;
        background: white;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-bottom: 10px;
    }

    .event-title {
        font-weight: 700;
        font-size: 15px;
    }

    .event-message {
        color: #6b7280;
        margin-top: 4px;
        font-size: 14px;
    }

    .success-box {
        padding: 20px;
        border-radius: 15px;
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
    }

    .footer {
        text-align: center;
        color: #9ca3af;
        margin-top: 40px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.markdown("## ✈️ FlowPilot")

    st.markdown(
        """
        **Autonomous AI Workflow Engineer**

        Plan → Execute → Observe → Repair → Verify
        """
    )

    st.divider()

    st.markdown("### AI Engine")

    st.success("Qwen3 1.7B")
    st.success("Local AI")
    st.success("Agent Online")

    st.divider()

    st.markdown("### Capabilities")

    st.write("🧠 AI Planning")
    st.write("⚙️ Tool Execution")
    st.write("🔧 Self-Repair")
    st.write("👁️ Verification")


# -----------------------------
# HERO
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-title">✈️ FlowPilot</div>
        <div class="hero-subtitle">
            Autonomous AI Workflow Engineer
        </div>

        <br>

        <div class="hero-subtitle">
            Give FlowPilot a goal and let the agent
            plan, execute, recover and verify it automatically.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# GOAL
# -----------------------------
st.markdown("### 🎯 Workflow Goal")

goal = st.text_area(
    "",
    value="Find AI internships for engineering students and create a short report.",
    height=100,
)


run = st.button(
    "🚀 Run Autonomous Workflow",
    type="primary",
    use_container_width=True,
)


# -----------------------------
# EXECUTION
# -----------------------------
if run:

    if not goal.strip():
        st.warning("Please enter a goal.")
        st.stop()

    st.divider()

    with st.spinner("FlowPilot is thinking and executing..."):

        output = execute_workflow(goal)

    logs = output["logs"]
    result = output["result"]
    observation = output["observation"]

    # -----------------------------
    # METRICS
    # -----------------------------
    successful_events = sum(
        1 for event in logs
        if event["status"] == "success"
    )

    failures = sum(
        1 for event in logs
        if event["status"] == "error"
    )

    repairs = sum(
        1 for event in logs
        if event["stage"] == "REPAIR AGENT"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">EVENTS</div>
                <div class="metric-value">{len(logs)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">SUCCESSFUL</div>
                <div class="metric-value">{successful_events}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">FAILURES</div>
                <div class="metric-value">{failures}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">REPAIRS</div>
                <div class="metric-value">{repairs}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------
    # EXECUTION TIMELINE
    # -----------------------------
    st.markdown("### 🔄 Agent Execution Timeline")

    for event in logs:

        if event["status"] == "error":
            icon = "❌"
        elif event["status"] == "success":
            icon = "✅"
        else:
            icon = "🔵"

        st.markdown(
            f"""
            <div class="event">
                <div class="event-title">
                    {icon} {event["stage"]}
                </div>

                <div class="event-message">
                    {event["message"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------
    # SUCCESS
    # -----------------------------
    if observation["status"] == "success":

        st.markdown(
            """
            <div class="success-box">
                <h3>✅ Workflow Successfully Completed</h3>
                <p>
                FlowPilot detected the failure, selected a recovery
                strategy and verified the final result.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------
    # FINAL RESULT
    # -----------------------------
    st.markdown("### 📋 Final Result")

    st.json(result)

    # -----------------------------
    # AI WORKFLOW PLAN
    # -----------------------------
    with st.expander("🧠 View AI-Generated Workflow"):

        st.write(output["workflow"])

    # -----------------------------
    # OBSERVER
    # -----------------------------
    with st.expander("👁️ View Verification"):

        st.json(observation)


# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    """
    <div class="footer">
        FlowPilot
        <br>
        Plan → Execute → Observe → Repair → Verify
    </div>
    """,
    unsafe_allow_html=True,
)
