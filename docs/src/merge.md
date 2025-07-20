# Merge

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/HK8brId7qQM?si=8_kX1z-hD5DC9B2m" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Next we'll cover how to merge two DataFrames together into a combined table.

We'll pull `faa-survey.csv`, which contains annual estimates of how many hours each type of helicopter was in the air. If we merge it with our accident totals, we will be able to calculate an accident rate.

We can read it in the same way as the NTSB accident list, with `read_csv`.

```python
# %%
import pandas as pd

# Load and prepare the accident data
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index().rename(columns={0: "accidents"})

# Load the FAA survey data
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
print("Survey data loaded successfully")
```

When joining two tables together, the first step is to look carefully at the columns in each table to find one they have in common and can serve as the basis for the join. We can do that with the `info` command we learned earlier.

```python
# %%
print("Accident counts structure:")
accident_counts.info()
```

```python
# %%
print("Survey data structure:")
survey.info()
```

You can see that each table contains the `latimes_make_and_model` column. We can therefore join the two files using that column with the pandas [`merge`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) method.

```{note}
If you are familar with traditional databases, you may recognize that the merge method in pandas is similar to [SQL’s JOIN statement](https://en.wikipedia.org/wiki/Join_(SQL)). If you dig into [merge’s documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html) you will see it has many of the same options.
```

Merging two DataFrames is as simple as passing both to pandas' built-in `merge` method and specifying which field you’d like to use to connect them. We will save the result into another new variable, which I'm going to call `merged_list`.

```{code-cell}
:tags: [show-input]
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
```

```{note}
You may notice something new with the `on="latimes_make_and_model"` bit above. It is what Python calls a [keyword argument](https://docs.python.org/3/glossary.html#term-argument). Keyword arguments are inputs passed to a function or method after explicitly specifying the name of the argument, followed by an equal sign.

Keyword arguments can be passed in any order, as long as the name of the argument is specified. When creating a function, they can be used to specify a default value for a parameter. For this reason, they are commonly used to provide overrides of a method's out-of-the-box behavior.

The pandas documentation for [`merge`]([https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)) reveals all of the keyword options available, as well as their defaults.
```

That new DataFrame can be inspected like any other.

```python
# %%
print("Merged data:")
print(merged_list.head())
```

Gasp! There's nothing there! What happened? Let's go back and inspect the datasets we're trying to merge. The `head` command remains our trusty friend for this type of task.

First, there was the accident counts.

```python
# %%
print("Accident counts data:")
print(accident_counts.head())
```

Then, there was the FAA survey dataset.

```python
# %%
print("Survey data:")
print(survey.head())
```

It looks like even though the `latimes_make_and_model` column represents the same data in each dataset, the casing is messy in the FAA survey data. Raw data is usually messy (even if this particular example is contrived). It's always important to inspect your data thoroughly and know how to clean it up before analyzing.

Since the uppercase accident counts data is more consistent, let's modify the FAA data to match. There are a handful of ways to do this, but the most straightforward is simply replacing everything in the `latimes_make_and_model` column with an uppercase copy of itself, as we did with the accident data in an earlier chapter. Once again, the `str` method can do the job.

```python
# %%
survey["latimes_make_and_model"] = survey["latimes_make_and_model"].str.upper()
print("Survey data converted to uppercase")
```

Now let's try merging our data again.

```python
# %%
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
print("Merge completed successfully")
```

And then take a peek.

```python
# %%
print("Merged data:")
print(merged_list.head())
```

Much better! By looking at the columns, you can check how many rows survived the merge, a precaution you should take every time you join two tables.

```python
# %%
print("Merged data info:")
merged_list.info()
```

You can also verify that the DataFrame has the same number of records as there are values in `accident_totals` column. That's good; if there are no null values, that means that every record in each DataFrame found a match in the other.

Another simple approach is to simply ask pandas to print the number of rows in the DataFrame. That can be done with the `len` function.

```python
# %%
print(f"Number of rows in merged data: {len(merged_list)}")
```

That number should match the number of rows in the accident totals DataFrame.

```python
# %%
print(f"Number of rows in accident counts: {len(accident_counts)}")
```

Now that we are confident we have a properly merged DataFrame, we're ready to move on to the next step: calculating the accident rate.