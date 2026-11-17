from src.query_engine import compile_query
from src.planner import rewrite


def test_compile_counts_stages():
    plan = compile_query("SELECT a FROM t WHERE a > 1", {"t": {}})
    assert "SELECT" in plan.stages and "WHERE" in plan.stages


def test_rewrite_drops_unsafe_join():
    plan = compile_query("SELECT a FROM t JOIN u ON t.id = u.id", {"t": {}, "u": {}})
    rewritten = rewrite(plan, {"join_columns": []})
    assert "JOIN" not in rewritten.stages
