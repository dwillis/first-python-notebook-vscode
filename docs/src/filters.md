# Filter

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/_Yfda9nIzVo?si=K4i1T6DQWfljTZjl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

The most common way to filter a DataFrame is to pass an expression as an “index” that can be used to decide which records to keep and which to discard. You write the expression by combining a column of your DataFrame with an “operator” like `==` or `>` or `<` and a value to compare each row against.

```{note}
If you are familiar with writing [SQL](https://en.wikipedia.org/wiki/SQL) to manipulate databases, pandas’ filtering system is somewhat similar to a WHERE query. The [official pandas documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#where) offers direct translations between the two.
```

Let's try filtering against the `state` field. Save a state's postal code into a variable. This will allow us to reuse it later.

```python
# %%
import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()

# Set a state to filter by
my_state = "IA"
print(f"Filtering data for state: {my_state}")
```

In the next section we will ask pandas to narrow down our list of accidents to just those in our state of interest. We will create a filter expression and place it between two square brackets following the DataFrame we wish to filter.

```python
# %%
filtered_accidents = accident_list[accident_list["state"] == my_state]
print(filtered_accidents)
```

Now we should save the results of that filter into a new variable separate from the full list we imported from the CSV file. Since it includes only accidents in our chosen state, let’s call it `my_accidents`.

```python
# %%
my_accidents = accident_list[accident_list["state"] == my_state]
print(f"Found {len(my_accidents)} accidents in {my_state}")
```

To check our work and find out how many records are left after the filter, let's run the DataFrame inspection commands we learned earlier.

First `head`.

```python
# %%
print("First few accidents in the filtered data:")
print(my_accidents.head())
```

Then `info`.

```python
# %%
print("Information about the filtered data:")
my_accidents.info()
```

Now pick another state and try running the code again. See if you can write filters that will answer the following questions:

1. Which state recorded more accidents: Iowa or Missouri?
2. How many accidents recorded more than one fatality?
3. How many accidents happened in California in 2015?
4. What percentage of the total fatalities occured in California?

Once you’ve written code that generates the answers, you’re ready to move on to the next chapter.