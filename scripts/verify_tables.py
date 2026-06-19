from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

means = pd.read_csv(DATA / "matched_budget_allocation_means.csv")
contrasts = pd.read_csv(DATA / "matched_budget_global_allocation_contrasts.csv")
doubling = pd.read_csv(DATA / "matched_budget_doubling_effects.csv")

assert len(means) == 6
assert set(means["budget"]) == {6400, 12800}
assert set(means["pair_count"]) == {50, 100, 200}
assert (means["n_cells"] == 40).all()

expected_reps = {
    (6400, 50): 128,
    (6400, 100): 64,
    (6400, 200): 32,
    (12800, 50): 256,
    (12800, 100): 128,
    (12800, 200): 64,
}
realized = {
    (int(r.budget), int(r.pair_count)): int(r.anchor_repetitions_requested)
    for r in means.itertuples()
}
assert realized == expected_reps

assert len(contrasts) == 6
assert set(contrasts["budget"]) == {6400, 12800}
assert set(contrasts["comparison"]) == {
    "100_minus_50",
    "200_minus_50",
    "200_minus_100",
}
assert (contrasts["n_seed_blocks"] == 10).all()

indexed = contrasts.set_index(["budget", "comparison"])
strong = indexed.loc[(6400, "200_minus_50")]
assert strong["mean_difference"] > 0
assert strong["bootstrap_ci_025"] > 0
assert strong["fraction_seed_blocks_positive"] == 1
assert abs(strong["exact_sign_flip_p_two_sided"] - 0.001953) < 1e-12

for budget in (6400, 12800):
    plateau = indexed.loc[(budget, "200_minus_100")]
    assert abs(plateau["mean_difference"]) < 0.003

assert len(doubling) == 4
assert (doubling["comparison"] == "12800_minus_6400").all()
assert (doubling["n_seed_blocks"] == 10).all()
assert (doubling["mean_difference"] > 0).all()
assert (doubling["bootstrap_ci_025"] > 0).all()

overall = doubling[doubling["scope"] == "overall"].iloc[0]
assert overall["pair_count"] == -1
assert overall["fraction_seed_blocks_positive"] == 1
assert abs(overall["mean_difference"] - 0.037357) < 1e-9

print("Matched-budget evidence tables verified.")
