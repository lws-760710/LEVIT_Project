from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class PlanningState(TypedDict):
    objective: str
    plan: str



def draft_plan(state: PlanningState) -> PlanningState:
    """Seed a minimal planning response for future graph expansion."""

    return {
        "objective": state["objective"],
        "plan": f"Initial plan prepared for: {state['objective']}",
    }



def build_planning_graph() -> StateGraph[PlanningState]:
    graph = StateGraph(PlanningState)
    graph.add_node("draft_plan", draft_plan)
    graph.add_edge(START, "draft_plan")
    graph.add_edge("draft_plan", END)
    return graph
