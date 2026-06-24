# PathoAlign pair-repeat allocation study

This repository is a focused study package for the PathoAlign pair-repeat allocation experiment.

## Positioning

I use PathoAlign to make a representation-identifiability claim: paired acquisitions can be used to factor frozen pathology embeddings into a scanner-suppressed tissue factor and an acquisition-specific factor.

This repository tests a narrower resource-allocation question inside that framework: when the total number of pair presentations is held fixed, does the factorization benefit more from seeing more unique biological pairs or from repeatedly anchoring fewer pairs?

## Study question

Under matched total pair-presentation budget, does spending budget on more unique biological pairs improve the biological representation more than spending the same budget on repeated anchors?

## Supported claim

Under matched total pair-presentation budgets of 6,400 and 12,800 pair presentations, increasing biological pair diversity improves PathoAlign biological consistency and factor separation relative to low-diversity/high-repetition anchor allocation, with a plateau from 100 to 200 pairs. Doubling the total budget from 6,400 to 12,800 also improves the biological score.

I interpret this as evidence that PathoAlign benefits from diverse paired biological correspondences rather than merely exploiting repeated anchors or a degenerate pair-memorization shortcut.

This is a representation-identifiability and resource-allocation study. It is research-only and does not support clinical or diagnostic claims.

## Frozen evidence tables

- `data/matched_budget_allocation_means.csv`
- `data/matched_budget_global_allocation_contrasts.csv`
- `data/matched_budget_doubling_effects.csv`

## Claim boundary

Safe:

> Increasing unique biological pair diversity improved PathoAlign factor-separation metrics under matched total pair-presentation budgets in this controlled allocation study.

Safe:

> The result is consistent with a paired-correspondence learning effect rather than simple repeated-anchor memorization.

Not safe:

> This proves disease biology.

Not safe:

> This establishes clinical or diagnostic validity.

Not safe:

> This proves complete biological/acquisition factor separation.

## Main research hub

https://github.com/matthewvaishnav/computational-pathology-research
