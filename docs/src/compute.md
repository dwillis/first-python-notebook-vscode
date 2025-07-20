# Compute

# Compute

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/JEzzfG8DetU?si=7dkoC3mqkk2WVCm8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

```python
# %%
# Setup data for computation examples
import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
survey["latimes_make_and_model"] = survey["latimes_make_and_model"].str.upper()
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
print("Data prepared for computation")
```

To calculate an accident rate, we'll need to create a new column based on the data in other columns, a process sometimes known as "computing."

In many cases, it's no more complicated than combining two Series using a mathematical operator. That's true in this case, where our goal is to divide the total number of accidents in each row by the total hours. That can accomplished with the following:

```python
# %%
print("Accident rate calculation:")
print(merged_list["accidents"] / merged_list["total_hours"])
```

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
survey["latimes_make_and_model"] = survey["latimes_make_and_model"].str.upper()
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
```

To calculate an accident rate, we’ll need to create a new column based on the data in other columns, a process sometimes known as “computing.”

In many cases, it’s no more complicated than combining two Series using a mathematical operator. That's true in this case, where our goal is to divide the total number of accidents in each row by the total hours. That can accomplished with the following:

```{code-cell}
:tags: [show-input]
merged_list["accidents"] / merged_list["total_hours"]
```

The resulting Series can be added to your DataFrame by assigning it to a new column. Name your column by providing it as a quoted string inside of square brackets. Let's call this column something brief and clear like `per_hour`.

```python
# %%
merged_list["per_hour"] = merged_list["accidents"] / merged_list["total_hours"]
print("Per hour column added")
```

Like everything else, you can inspect with the `head` command.

```python
# %%
print("Data with per hour column:")
print(merged_list.head())
```

You can see that the result is in [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation). As is common when calculating per capita statistics, let's multiple the per-hour results by a common number to make the figures more legible. That's as easy as tacking some multiplication at the end of a computation. Here we'll multiply by 100,000 hours.

```python
# %%
merged_list["per_100k_hours"] = merged_list["per_hour"] * 100_000
print("Per 100k hours column added")
```

Have a look at the result with `head` again.

```python
# %%
print("Final data with computed accident rates:")
print(merged_list.head())
```

Much better! Now lets move on to the next step, sorting our data into a ranking.