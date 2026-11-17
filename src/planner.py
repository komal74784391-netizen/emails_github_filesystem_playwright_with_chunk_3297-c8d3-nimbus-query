"""Cost-based planner for Nimbus Query."""

from src.query_engine import Plan


def rewrite(plan: Plan, statistics: dict) -> Plan:
    remaining = []
    for stage in plan.stages:
        if stage == "JOIN" and not statistics.get("join_columns"):
            continue
        remaining.append(stage)
    return Plan(stages=remaining, estimated_cost=max(plan.estimated_cost - 0.5, 0.0))
