from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


means = read_csv("matched_budget_allocation_means.csv")
contrasts = read_csv("matched_budget_global_allocation_contrasts.csv")
doubling = read_csv("matched_budget_doubling_effects.csv")

assert len(means) == 6
assert {int(r["budget"]) for r in means} == {6400, 12800}
assert {int(r["pair_count"]) for r in means} == {50, 100, 200}
assert all(int(r["n_cells"]) == 40 for r in means)

expected_reps = {
    (6400, 50): 128,
    (6400, 100): 64,
    (6400, 200): 32,
    (12800, 50): 256,
    (12800, 100): 128,
    (12800, 200): 64,
}
realized = {
    (int(r["budget"]), int(r["pair_count"])): int(r["anchor_repetitions_requested"])
    for r in means
}
assert realized == expected_reps

assert len(contrasts) == 6
assert {int(r["budget"]) for r in contrasts} == {6400, 12800}
assert {r["comparison"] for r in contrasts} == {
    "100_minus_50",
    "200_minus_50",
    "200_minus_100",
}
assert all(int(r["n_seed_blocks"]) == 10 for r in contrasts)

indexed = {
    (int(r["budget"]), r["comparison"]): r
    for r in contrasts
}

strong = indexed[(6400, "200_minus_50")]
assert float(strong["mean_difference"]) > 0
assert float(strong["bootstrap_ci_025"]) > 0
assert float(strong["fraction_seed_blocks_positive"]) == 1
assert abs(float(strong["exact_sign_flip_p_two_sided"]) - 0.001953) < 1e-12

for budget in (6400, 12800):
    plateau = indexed[(budget, "200_minus_100")]
    assert abs(float(plateau["mean_difference"])) < 0.003

assert len(doubling) == 4
assert all(r["comparison"] == "12800_minus_6400" for r in doubling)
assert all(int(r["n_seed_blocks"]) == 10 for r in doubling)
assert all(float(r["mean_difference"]) > 0 for r in doubling)
assert all(float(r["bootstrap_ci_025"]) > 0 for r in doubling)

overall = [r for r in doubling if r["scope"] == "overall"][0]
assert int(overall["pair_count"]) == -1
assert float(overall["fraction_seed_blocks_positive"]) == 1
assert abs(float(overall["mean_difference"]) - 0.037357) < 1e-9

print("Matched-budget evidence tables verified.")
