---
jupytext:
  texWe'll begin with the `latimes_makThere's another built-in pandas tool that will total up the frequency of values in a column. The method is called [`value_counts`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html) and it's just as easy to use as `sum`, `min` or `max`. All you need to do it is add a period after the column name and chain it on the tail end of your code.

```python
# %%
print(accident_list["latimes_make_and_model"].value_counts())
```model` column, which records the standardized name of each helicopter that crashed. To access its contents separate from the rest of the DataFrame, append a pair of square brackets with the column's name in quotes inside. 

```python
# %%
import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")

# Access a specific column
print(accident_list["latimes_make_and_model"])
```ion:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Columns

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/o_uJTbpMzJk?si=WFJS4fU5a9dl4j0w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

We’ll begin with the `latimes_make_and_model` column, which records the standardized name of each helicopter that crashed. To access its contents separate from the rest of the DataFrame, append a pair of square brackets with the column’s name in quotes inside. 

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
```

```{code-cell}
:tags: [show-input]
accident_list["latimes_make_and_model"]
```

That will list the column out as a `Series`, just like the ones we created from scratch earlier. Just as we did then, you can now start tacking on additional methods that will analyze the contents of the column.

````{note}
You can also access columns a second way, like this: `accident_list.latimes_make_and_model`. This method is quicker to type, but it won't work if your column has a space in its name. So we're teaching the universal bracket method instead.
````

## Count a column's values

In this case, the column is filled with characters. So we don’t want to calculate statistics like the median and average, as we did before.

There’s another built-in pandas tool that will total up the frequency of values in a column. The method is called [`value_counts`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html) and it’s just as easy to use as `sum`, `min` or `max`. All you need to do it is add a period after the column name and chain it on the tail end of your cell.

```{code-cell}
:tags: [show-input]
accident_list["latimes_make_and_model"].value_counts()
```

Congratulations, you've made your first finding. With that little line of code, you've calculated an important fact: During the period being studied, the Robinson R44 had more fatal accidents than any other helicopter.

But wait. Before we congratulate ourselves, let's take a closer look at the data. Our value counts operation has turned up an imperfection that was buried in the data. Can you see it?

## Cleaning data columns

On closer inspection, we can see that Bell 206 helicopter is listed two different ways, as `BELL 206` and `bell 206`. The variation in capitalization is causing pandas to treat them as two distinct values.

This is a common problem and a simple example of how "dirty" data can trip up a computer program. The solution is to clean up the column prior to analysis.

In this case, we can use the `str` method, which is short for string. In many computer programming languages, string is the technical term used to refer to text. Thus, the pandas `str` method is designed to manipulate a column of text. It can change the casing of text, find and replace different patterns and conduct many other useful operations.

You can access it by chaining `.str` and your desired manipulation method after the column name. In this case, we want to use the `upper` method, which will convert all of the text in the column to uppercase.

```python
# %%
print("Converting to uppercase:")
print(accident_list["latimes_make_and_model"].str.upper())
```

While it's not useful in this case, we can try out the companion `lower` method to see it do the opposite.

```python
# %%
print("Converting to lowercase:")
print(accident_list["latimes_make_and_model"].str.lower())
```

```{note}
You can find a full list of `str` methods, along with useful examples, in the [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods).
```

To correct the bug, we need to assign the result of the `upper` method to our existing column and overwrite what's there. We can do that with the `=` operator.

```python
# %%
accident_list["latimes_make_and_model"] = accident_list["latimes_make_and_model"].str.upper()
print("Column has been converted to uppercase")
```

Now we can run `value_counts` again to see if the problem has been fixed.

```python
# %%
print("Value counts after cleaning:")
print(accident_list["latimes_make_and_model"].value_counts())
```

Much better! We have a clean list of helicopter models and their frequencies.

In the real world, you will almost always need to clean your data before you can analyze it, though the challenges will typically be more complex than this one. Pandas offers a wide range of tools to help you clean your data, but the basic process is always the same: Identify the problem, fix it, and then check your work. The `value_counts` method is one of the most useful tools in this process.

Before we move on to the next chapter, here's a challenge. See if you can answer a few more questions a journalist might ask about our dataset. All of the questions below can be answered using only tricks we've covered thus far.

1. What was the total number of fatalities?
2. Which helicopter maker had the most fatal accidents?
3. Which year had the most fatal helicopter accidents?
4. How many fatal helicopter accidents occurred in Texas?
5. How many different helicopter makers are in the dataset?

Once you’ve written code that generates the answers, you’re ready to move on to the next chapter.