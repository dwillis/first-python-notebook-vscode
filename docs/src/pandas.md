---
jupytext:
  text_representation:
    extension: .md
    formaWe can start to get a look at its powers by converting that plain Python list into what pandas calls a [Series](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html). Here's how to make it happen in your next section. Let's stick with simple variables and name it `my_series`._name: myst
    format_versio   n: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Pandas

```{note}
**Interactive Version Available**: This chapter is also available as an interactive Jupyter notebook. You can find it in the [Interactive Notebooks](notebooks/index.md) section as `pandas.ipynb`. The notebook version allows you to run the code directly and experiment with the examples.
```

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/6Bi3NS3fBk0?si=TGmkKNwl0jbvDHhO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Python is filled with functions to do pretty much anything you’d ever want to do with a programming language: [navigate the web](http://docs.python-requests.org/), [parse data](https://docs.python.org/2/library/csv.html), [interact with a database](http://www.sqlalchemy.org/), [run fancy statistics](https://www.scipy.org/), [build a pretty website](https://www.djangoproject.com/) and [so](https://www.crummy.com/software/BeautifulSoup/) [much](http://www.nltk.org/) [more](https://pillow.readthedocs.io/en/stable/).

Creative people have put these tools to work to get [a wide range of things done](https://www.python.org/about/success/) in the academy, the laboratory and even in outer space. Some are included in a toolbox that comes with the language, known as the standard library. Others have been built by members of Python’s developer community and need to be downloaded and installed from the web.

![pandas on PyPI](https://palewi.re/docs/first-python-notebook/_static/img/pandas-pypi.png)

One third-party tool that's important for this class is called [pandas](http://pandas.pydata.org/). It was invented for use at a [financial investment firm](https://www.aqr.com/) and has become the leading open-source library for accessing and analyzing data in many different fields.

## Import pandas

Add the following to your Python file (or create a new cell if you're using the interactive mode). Type in the following and run it:

```python
# %%
import pandas
```

If nothing happens, that's good. It means you have pandas installed and ready to use.

```{note}
Since pandas is created by a third party independent from the core Python developers, it wouldn't be installed by default in a basic Python installation.

If you followed the VS Code setup chapter and used uv to set up your project, pandas should already be installed. If your Python environment doesn't have pandas, you can install it by opening the VS Code terminal (`View > Terminal`) and running `uv add pandas`.
```

Return to your import section and rewrite it like this:

```python
# %%
import pandas as pd
```

This will import the pandas library at the shorter variable name of `pd`. This is standard practice in the pandas community. You will frequently see examples of pandas code online using `pd` as shorthand. It's not required, but it's good to get in the habit so that your code is more likely to be quickly understood by other computer programmers.

```{note}
In Python, a variable is a way to store a value in memory for later use. A variable is a named location in the computer's memory where a value can be stored and retrieved. Variables are used to store data values, such as numbers, strings, lists, or objects, and they can be used throughout the program to refer to the stored value.

To create your own variable in Python, you use the assignment operator (`=`) to assign a value to a variable. The variable name is on the left side of the assignment operator and the value is on the right side.
```

## Conduct a simple data analysis

Those two little letters contain dozens of data analysis tools that we'll use in future lessons. They can read in millions of records, compute advanced statistics, filter, sort, rank and do just about anything else you'd want to do with data.

As we saw with the list in the last chapter, Python can do quite a bit on its own. The advantage of pandas is that it saves time by offering even more options. 

We can start to get a look at its powers by converting that plain Python list into what pandas calls a [Series](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html). Here's how to make it happen in your next cell. Let’s stick with simple variables and name it `my_series`.

```python
# %%
# Create a list of numbers (from previous chapter)
my_list = [1, 3, 5, 7, 9, 999]

# Convert it to a pandas Series
my_series = pd.Series(my_list)
print(my_series)
```

Once the data becomes a Series, you can immediately run a wide range of [descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics). Let's try a few.

How about summing all the numbers? Add this to your next section and run it. It should output the total, just like the `sum()` function from the last chapter.

```{code-cell}
:tags: [show-input]
my_series.sum()
```

Then find the maximum value in the next.

```{code-cell}
:tags: [show-input]
my_series.max()
```

The minimum value in the next.

```{code-cell}
:tags: [show-input]
my_series.min()
```

How about the average?

```{code-cell}
:tags: [show-input]
my_series.mean()
```

And how about the median, which we didn't have a way to do with just Python?

```{code-cell}
:tags: [show-input]
my_series.median()
```

Let's go further. How about the standard deviation?

```{code-cell}
:tags: [show-input]
my_series.std()
```

Finally, all of the above, plus a little more about the distribution, in one simple command.

```{code-cell}
:tags: [show-input]
my_series.describe()
```

If you substituted in a series of 10 million records, your notebook would calculate all those same statistics without you needing to write any more code. Once your data, however large or complex, is imported into pandas, there's little limit to what you can do to filter, merge, group, aggregate, compute or chart using simple methods like the ones above. In the chapter to come we’ll start doing just using that with data from a real Los Angeles Times investigation.
