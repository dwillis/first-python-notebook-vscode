# Concatenate

```python
# %%
# Setup data for concatenation examples
import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
accident_counts = accident_list.groupby("latimes_make_and_model").size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
survey["latimes_make_and_model"] = survey["latimes_make_and_model"].str.upper()
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
print("Data prepared for concatenation examples")
```

Let's briefly pretend we've already completed our analysis, visualized and published our findings. A year later, there's more data. We want to follow up.

Let's crack open the old notebook and see what we can do.

```python
# %%
new_accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents-update.csv")
print("New accident data loaded")
```

Now that we've imported it, let's peek at the new data using our familiar `head()` method.

```python
# %%
print("New accident data preview:")
print(new_accident_list.head())
```

Okay, so we have three new accidents that we want to add in. But, hang on. Can you spot the differences in the data?

Our columns are in a slightly different order. This happens a lot from year to year in state datasets: a new data person starts, and they decide to reformat everything. But we've set everything up using the previous years' formatting style.

Luckily, Pandas has a built-in method for dealing with problems like this: `concat`. 

This method *concatenates* multiple DataFrames into a single DataFrame by combining their rows and columns.

```python
# %%
updated_accident_list = pd.concat([accident_list, new_accident_list])
print("DataFrames concatenated")
```

How do we check what this actually did? Let's take a quick look at our columns.

`count()` gives us a brief overview of how many non-null values we have in each column. If we did this right and our data is complete, we should have the same number of values in every column.

```python
# %%
print("Column counts after concatenation:")
print(updated_accident_list.count())
```

Hang on. That doesn't look right. Three values in `ntsb-model`, `ntsb-number`, and `total-fatalities`? It looks like we have the same total in other columns. But those three values should be combined with `ntsb_model` and so on, instead of on their own.

We need to change the column names from the 2024 data so they match previous years'. 

Luckily, there's a way to do that. 

Write out any column names you want to be changed in this format: 

```python
# %%
bad_columns = {"ntsb-model" : "ntsb_model",
               "ntsb-number" : "ntsb_number",
               "total-fatalities" : "total_fatalities"}
print("Column rename dictionary created")
```

This is called a `dictionary`. It's a [very useful data type](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) built into Python. It basically functions like a list, except each list item has a `key` that maps to a `value`. In our case, we'll be using the `key` to look for the current column name and the `value` to assign a new column name. 

That means the old names go to the left of the colon, and the new names go to the right. 

```{note}
Renaming columns in a dictionary can get really handy for larger datasets. You can even create a default, reusable dictionary that renames standard or common strings to your newsroom's house style, or that changes all instances of "number" to "#". This dataset is small, but when you start analyzing datasets with thousands of columns, this can save you a lot of pain.
```

Next, let's grab the DataFrame we originally imported the 2024 data into (`new_accident_list`) and apply our column-name cleaner to it *before* we concatenate it with the other data.

(If you rename the columns after concatenating, you'll just end up with two columns with the same name and different variables.)

```python
# %%
new_accident_list = new_accident_list.rename(columns=bad_columns)
print("Column names updated in new data")
```

Okay, let's see how that worked.

```python
# %%
print("Column counts in updated new data:")
print(new_accident_list.count())
```
*This* looks more like what we want to put together. 

Let's try the `concat` step again.

```python
# %%
updated_accident_list = pd.concat([accident_list, new_accident_list])
print("DataFrames concatenated with corrected column names")
```

And check our work with `count`.

```python
# %%
print("Final column counts after proper concatenation:")
print(updated_accident_list.count())
```

We now have 166 complete values and no split columns. This also reorders your columns for you automatically, because `concat` matches on the column name. It defaults to the column order in the DataFrame on the left; if you wanted to keep the `new_accident_list` order, you'd have to swap the order in the `concat` command.

And now we can re-run our whole analysis with a fresh year of data added in — without changing anything except the name of the DataFrame it's operating on. 

We could also overwrite our original DataFrame with the new data so we don't even have to change the DataFrame name to re-run the analysis. But that can be risky if you don't keep track of your order of operations and leave good notes for yourself.
