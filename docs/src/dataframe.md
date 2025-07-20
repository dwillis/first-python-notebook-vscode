---
jupytext:
  text_representation:
    extension```{warning}
You need the You shouldn't see anything. That's a good thing. It means our DataFrame has been saved under the name `accident_list`, which we can now begin interacting with in the following sections.

We can do this by calling ["methods"](https://en.wikipedia.org/wiki/Method_(computer_programming)) that pandas makes available to all DataFrames. You may not have known it at the time, but `read_csv` is one of these methods. There are dozens more that can do all sorts of interesting things. Let's start with some easy ones that analysts use all the time.

## The `head` method

To preview the first few rows of the dataset, try the [`head`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html) method. Add a new section, type this in and run it.

```python
# %%
print(accident_list.head())
```ared in the example to access the file. While you could laboriously type it out, feel free to copy and paste it into your code.
```

After you run the code, you should see a big table output in VS Code's Interactive Window (if using interactive cells) or printed to the terminal. It is a "DataFrame" where pandas has structured the CSV data into rows and columns, just like Excel or other spreadsheet software might. Take a moment to look at the columns and rows in the output, which contain the data we'll use in our analysis.
    format_name: myst
    format_version: '0.8'
    jupytext_version: '1.4.1'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Data

In 2018, the Los Angeles Times published an investigation headlined, [“The Robinson R44, the world’s best-selling civilian helicopter, has a long history of deadly crashes.”](https://www.latimes.com/projects/la-me-robinson-helicopters/)

![jupyterlab desktop download](/_static/R44-story.png)

It reported that Robinson’s R44 led all major models with the highest fatal accident rate from 2006 to 2016. The analysis was [published on GitHub](https://github.com/datadesk/helicopter-accident-analysis) as a series of Jupyter notebooks.

The findings were drawn from two key datasets:

1. The National Transportation Safety Board's [Aviation Accident Database](https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx)
2. The Federal Aviation Administration's [General Aviation and Part 135 Activity Survey](https://www.faa.gov/data_research/aviation_data_statistics/general_aviation/)

After a significant amount of work gathering and cleaning the source data, the number of accidents for each helicopter model were normalized using the flight hour estimates in the survey. For the purposes of this demonstration, we will read in tidied versions of each file that are ready for analysis.

The data are structured in rows of comma-separated values. This is known as a [CSV file](https://en.wikipedia.org/wiki/Comma-separated\_values). It is the most common way you will find data published online. The pandas library is able to read in files from a variety formats, including CSV.

```{code-cell}
:tags: [hide-cell]

import pandas as pd
```

## The `read_csv` method

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/XWqRkIx-BzQ?si=tXxS-F_KdzOIbp1F" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Start by adding the following code to your Python file (or create a new cell if you're using interactive mode). We'll import the first CSV file using the [`read_csv`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) function included with pandas.

```python
# %%
import pandas as pd
pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
```

```{warning}
You need the exact URL shared in the example to access the file. While you could laboriously type it out, feel free to copy and paste it into your notebook.
```

After you run the cell, you should see a big table output to your notebook. It is a “DataFrame” where pandas has structured the CSV data into rows and columns, just like Excel or other spreadsheet software might. Take a moment to look at the columns and rows in the output, which contain the data we'll use in our analysis.

```{note}
On the left-hand side, you'll see a bolded number incrementing upward from zero that's not present in our source data file. This is what pandas calls the [index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html). It is a separate column created automatically and used to identify each row. The index is not considered part of the data, but it is used to reference the rows of the DataFrame or Series in advanced operations that are beyond the scope of this class.
```

A major advantage of VS Code and Python scripting over spreadsheets is that rather than manipulating the data through a haphazard series of clicks and keypunches, we will be gradually grinding it down using a computer programming script that is transparent and reproducible.

To do more with your DataFrame, we need to store it so it can be reused in subsequent sections. We can do this by saving it in a variable, just as we did in with our `number` in Chapter 2.

Go back to your latest code section and change it to this. Run it again.

```python
# %%
import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
```

You shouldn't see anything. That's a good thing. It means our DataFrame has been saved under the name `accident_list`, which we can now begin interacting with in the following cells.

We can do this by calling ["methods"](https://en.wikipedia.org/wiki/Method_(computer_programming)) that pandas makes available to all DataFrames. You may not have known it at the time, but `read_csv` is one of these methods. There are dozens more that can do all sorts of interesting things. Let’s start with some easy ones that analysts use all the time.

## The `head` method

To preview the first few rows of the dataset, try the [`head`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html) method. Add a new cell, type this in and hit the play button again.

```{code-cell}
:tags: [show-input]
accident_list.head()
```

It serves up the first five rows by default. If you want a different number, submit it as an input.

```python
# %%
print(accident_list.head(1))
```

## The `info` method

To get a look at all of the columns and what type of data they store, add another section and try the [info](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html) method. Look carefully at the results and you'll see we have 163 fatal accidents to review.

```python
# %%
print(accident_list.info())
```

Now that you've got some data imported, we’re ready to begin our analysis.
