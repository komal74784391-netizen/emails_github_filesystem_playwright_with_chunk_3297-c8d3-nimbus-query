"""Execution entry point for the Nimbus query engine."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Plan:
    stages: list
    estimated_cost: float


def compile_query(sql: str, catalog: dict) -> Plan:
    tokens = sql.replace("(", " ( ").replace(")", " ) ").split()
    stages = []
    for token in tokens:
        if token.upper() in {"SELECT", "FROM", "WHERE", "JOIN"}:
            stages.append(token.upper())
    cost = round(len(stages) * 0.75 + len(catalog) * 0.1, 3)
    return Plan(stages=stages, estimated_cost=cost)
