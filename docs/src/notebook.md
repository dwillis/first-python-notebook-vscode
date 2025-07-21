# Working with Python in VS Code

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe"  src="https://www.youtube.com/embed/VqCgcpAypFQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Now that you have VS Code set up with Python and all required packages, it's time to start writing and running Python code. This chapter will teach you the fundamentals of Python programming using VS Code's interactive features.

```{note}
**Prerequisites**: Make sure you've completed the [VS Code Setup](vscode_setup.md) chapter first. You should have:
- VS Code installed with Python and Jupyter extensions
- uv installed and a `first-python-notebook` project created
- All required packages (pandas, matplotlib, seaborn, jupyter, altair) installed
- VS Code opened in your project directory
```

## Your First Python Program

Let's start by creating your first Python file. In VS Code:

1. Press `Ctrl+N` (or `Cmd+N` on Mac) to create a new file
2. Save it as `my_first_analysis.py` by pressing `Ctrl+S` (or `Cmd+S` on Mac)

You should see an empty editor window. Let's start with some simple math. Type the following into the editor, then right-click and select "Run Python File in Terminal" or press `F5`:

```python
print(2+2)
```

The number four should appear in the terminal at the bottom of the screen. Congratulations! You've just written your first line of code. In Python terminology, you've used two [integers](https://docs.python.org/3/library/functions.html#int) and combined them with [the addition operator](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions).

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/g_pJejF0GmU?si=Dw5X91-vINPaSBOQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Now try writing your own math problem. Maybe `print(2+3)` or `print(2+200)`. After you've typed it in, run the file again to see the result.

### Understanding Errors

If you get an error when running your code, don't worry! Code errors are a normal part of programming. Here's an example of an error:

```python
print(2+2+)  # This has an error!
```

This will cause an error because the addition operator needs a number after it. The correct version would be:

```python
print(2+2+2)  # This works correctly
```

The best approach when you encounter errors is to remain calm and carefully read the error message - it usually contains helpful clues for fixing the problem.

## Interactive Python Development

VS Code also supports interactive Python development similar to Jupyter notebooks. You can use this feature by adding special comment markers to create "cells" in your Python file.

Add the following to your file:

```python
# %%
# This is an interactive cell
number = 2
print(f"My number is: {number}")

# %%
# This is another cell
result = number + 3
print(f"The result is: {result}")
```

When you add `# %%` comments, VS Code will show "Run Cell" buttons above each section. Click these buttons to run individual sections of code interactively. This opens the Interactive Python window where you can see the output, similar to a Jupyter notebook but integrated into VS Code.

Over time you will gradually build up your analysis by adding more code sections. A simple example is storing your number in a variable in one cell:

```python
# %%
number = 2
```

Then adding it to another value in the next cell:

```python
# %%
print(number + 3)
```

Run those two cells in succession and VS Code should output the number 5 in the Interactive window.

Change the `number` value to 3 and run both cells again. Instead of 5, it should now output 6.

So, first this:

```python
# %%
number = 3
```

Then this:

```python
# %%
print(number + 3)
```

Now try defining your own numeric variable and doing some math with it. You can name it whatever you want. Want to try some other math operations? The `-` sign does subtraction. Multiplication is `*`. Division is `/`.

Sometimes it is helpful to describe what the code is doing in case you want to share it with a colleague or return to it after some time. You can add comments in your code by putting a hash `#` in front of the text. So, for example, we could use a comment to add extra information about the number variable.

```python
# %%
# This is a random number
number = 3
```

To add a new cell in VS Code, simply add another `# %%` comment where you want the new cell to begin. VS Code will automatically recognize this as a new interactive cell.

To organize your code better, you can also create markdown cells for documentation by using `# %% [markdown]`:

```python
# %% [markdown]
# # This is a heading
# This is some documentation about my analysis
# - Point one
# - Point two

# %%
# This is a code cell
print("Hello from the code cell!")
```

```{note}
If you've never written code before and are unfamiliar with variables, functions, or other programming concepts, we recommend ["An Informal Introduction to Python"](https://docs.python.org/3/tutorial/introduction.html) and subsequent sections of python.org's official tutorial.
```

## Working with Lists

Now let's make a list of numbers. A list is another tool Python offers for working with figures. Creating one is as simple as stringing together a set of values surrounded by square brackets and separated by commas. 

Let's start simple. Enter all of the even numbers between zero and ten. Name its variable something plain like `my_list`:

```python
# %%
my_list = [2, 4, 6, 8]
print(my_list)
```

You can do cool stuff with any list, even calculate statistics. One built-in Python function that's always available is `sum`, which adds up all the items in the list.

```python
# %%
print(sum(my_list))
```

Another is `len`, an abbreviation for length, which returns how many values are contained in the list.

```python
# %%
print(len(my_list))
```

Using the simple math operators we explored earlier, you can calculate the basic formula for an average by dividing the result of those two options:

```python
# %%
average = sum(my_list) / len(my_list)
print(f"The average is: {average}")
```

Now go back to your list and replace the even numbers with all of the odds between zero and ten. When you rerun all the subsequent cells your statistics should update to reflect the new values.

```python
# %%
my_list = [1, 3, 5, 7, 9]
print(f"New list: {my_list}")
```

Add a very large number like 999 to the end of the list and you should see your average value shoot way up, a common issue in statistics called an outlier or a skew.

```python
# %%
my_list = [1, 3, 5, 7, 9, 999]
print(f"List with outlier: {my_list}")
print(f"New average: {sum(my_list) / len(my_list)}")
```

The most common way to address that problem in journalism is to substitute in a different statistic for the average, typically a median. While a skilled Python programmer could conjure up some code to run that calculation here, there's no simple built-in tool like `sum` or `len`.

## Working with Jupyter Notebooks in VS Code

VS Code also supports traditional Jupyter notebooks (.ipynb files), which provide a more interactive experience with rich output display. You can create one by:

1. Opening the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Typing "Jupyter: Create New Jupyter Notebook"
3. Pressing Enter

This creates a notebook file where you can add both code and markdown cells. VS Code provides the complete notebook experience including:
- Rich output display (plots, tables, HTML)
- Variable explorer
- Run cells individually or all at once
- Export to various formats
- All of VS Code's powerful editing features

```{tip}
**Quick Check**: Make sure the kernel name in the top-right corner of the notebook matches your project environment (should show `first-python-notebook` or similar). If you need to change it, click on the kernel name and select the correct environment.
```

```{note}
This tutorial includes a complete collection of interactive Jupyter notebooks that you can run directly in VS Code. You can find them in the [Interactive Notebooks](notebooks/index.md) section. These notebooks contain the same content as the tutorial chapters but in an interactive format where you can run the code and see the results immediately.
```

## Next Steps

Once you've got the hang of running Python code in VS Code, you're ready to introduce pandas, the powerful Python analysis library that can do a whole lot more than add a few numbers together.

You can continue with the traditional tutorial chapters or jump directly to the [Interactive Notebooks](notebooks/index.md) for a hands-on experience.
