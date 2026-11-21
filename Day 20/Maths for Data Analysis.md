---
aliases: [Logic and Problem-Solving - Day 20]
tags: [logic-and-problem-solving, term1, lecture-notes, data-analysis, probability, correlation]
course: "[[Logic and Problem-Solving]]"
day: 20
---

# Logic and Problem-Solving — Day 20: Maths for Data Analysis

**Today's focus:** use [[Probability Likelihood and Correlation|probability, likelihood, correlation and trends]] to pull answers out of a dataset (CSV files worked in Excel).

## Probability
Chance of an outcome = **favourable outcomes ÷ total outcomes**. Multiply by 100 for a percentage.

**Example — election_results.csv (Yellowknife):** `VotesForVictor / TotalVotes` = 7123 / 12345 = 0.577 → **57.7%** of the vote.

## Likelihood
Here likelihood is the **odds**: `P(X) / (1 − P(X))`. Probability alone says "how often"; likelihood says how many times more likely it is to happen than not.

**Example — medical_data.csv** (1 = positive, 0 = negative). Build an Excel pivot table of `ActualCondition` vs `TestResult`.

| Test result | Matches ÷ total tests | P(X) | Likelihood |
|---|---|---|---|
| Positive test is truly positive | 113 / 133 | 0.849 | 0.849 / 0.151 = **5.623** |
| Negative test is truly negative | 52 / 67 | 0.776 | 0.776 / 0.224 = **3.464** |

## Correlation
Do two variables move together? In Excel: `=CORREL(range1, range2)` gives the **r-value** (−1 to 1).
- Sign: positive (both rise), negative (one rises, other falls), ~0 = independent
- Size: closer to ±1 = stronger relationship

**Example:** `ActualCondition` vs `Age` → r = **0.572**, a moderate positive correlation. Older patients are more likely to have the condition.

> Correlation ≠ causation. Age is plausibly causal here (older people get more illnesses), but it needs further analysis to confirm.

## Trends
Chart the data and look for patterns over time (toy_sales.csv):
1. **Seasonal:** line chart of `Month` vs `Revenue` shows a jump October → December (Christmas gift buying)
2. **Growth:** pivot table/chart of `Year` vs `Units_Sold` shows sales rising every year. Possible causes: population growth, a strong economy, cheaper production

Always state the trend, the steps and a *possible* cause, and don't claim more than the data shows.

## To Know
- [ ] Probability formula, and converting to a percentage
- [ ] Likelihood = P / (1 − P)
- [ ] `CORREL`, reading r: direction, strength, causal or not
- [ ] Pivot tables and line charts for finding trends

## Homework
- Lesson 20 sample problems (election results, medical data correlation, toy sales trends)

## Reflection
*What was the most surprising insight today?*
