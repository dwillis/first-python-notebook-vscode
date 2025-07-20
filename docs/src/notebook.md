# Working with Python in VS Code

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe"  src="https://www.youtube.com/embed/VqCgcpAypFQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Once VS Code is installed with the Python extension, you're ready to start writing and running Python code. VS Code offers several ways to work with Python, from simple scripts to interactive notebook-style development.

Let's start by creating your first Python file. In VS Code:

1. Press `Ctrl+N` (or `Cmd+N` on Mac) to create a new file
2. Save it as `my_first_analysis.py` by pressing `Ctrl+S` (or `Cmd+S` on Mac)
3. Choose a location on your computer to save it

![VS Code new file](/_static/vscode-new-file.png)

```{note}
If VS Code prompts you to select a Python interpreter, choose the Python installation you set up in the previous chapter. This tells VS Code which Python environment to use when running your code.
```

Now you're ready to write your first line of Python code. VS Code provides an excellent environment for both learning and professional Python development.

You should see an empty editor window. That means you are all set up and ready to write Python. If you've never done it before, you can remain calm. We can start out slow with some simple math.

Type the following into the editor, then right-click and select "Run Python File in Terminal" or press `F5`. The number four should appear in the terminal at the bottom of the screen.

```python
print(2+2)
```

There. Not so bad, right? You have just written your first line of code. When you run a Python file, VS Code executes all the code in the file and displays the output in the integrated terminal. In the jargon of Python, you have entered two [integers](https://docs.python.org/3/library/functions.html#int) and combined them using [the addition operator](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions).

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/g_pJejF0GmU?si=Dw5X91-vINPaSBOQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Now try writing your own math problem. Maybe `print(2+3)` or `print(2+200)`. Whatever strikes your fancy. After you've typed it in, run the file again. This workflow of writing Python code and then running it is the rhythm of working with Python in VS Code.

If you get an error after you run your code, look carefully at your code and check whether it exactly matches what's been written in the example. Here's an example of an error that I've added intentionally:

```python
print(2+2+)
```

Don't worry. Code crashes are a normal part of life for computer programmers. They're usually caused by small typos that can be quickly corrected. 

```python
print(2+2+2)
```

The best thing you can do is remain calm and carefully read the error message. It usually contains clues that can help you fix the problem.

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

In addition to interactive Python files, VS Code also supports traditional Jupyter notebooks (.ipynb files). You can create one by:

1. Opening the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Typing "Jupyter: Create New Jupyter Notebook"
3. Pressing Enter

This creates a notebook file where you can add both code and markdown cells, just like in traditional Jupyter environments, but with all the benefits of VS Code's editor features.

The notebook interface in VS Code allows you to:
- Add code and markdown cells
- Run cells individually or all at once
- View rich output including plots and tables
- Export to various formats
- Use VS Code's powerful editing features

```{note}
This tutorial includes a complete collection of interactive Jupyter notebooks that you can run directly in VS Code. You can find them in the [Interactive Notebooks](notebooks/index.md) section. These notebooks contain the same content as the tutorial chapters but in an interactive format where you can run the code and see the results immediately.
```

## Next Steps

Once you've got the hang of running Python code in VS Code, you're ready to introduce pandas, the powerful Python analysis library that can do a whole lot more than add a few numbers together.

You can continue with the traditional tutorial chapters or jump directly to the [Interactive Notebooks](notebooks/index.md) for a hands-on experience.
