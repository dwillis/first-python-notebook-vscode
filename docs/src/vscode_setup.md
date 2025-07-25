# Visual Studio Code Setup

[Visual Studio Code](https://code.visualstudio.com/) is a free, open-source code editor developed by Microsoft. It has become one of the most popular development environments for Python programming, offering excellent support for data analysis, debugging, and interactive computing.

VS Code provides an integrated experience for Python development that combines the best of traditional code editing with full Jupyter notebook support. You can create and run Jupyter notebooks directly in the editor, write Python scripts with interactive cells, and leverage powerful debugging and version control tools all in one place.

It is used by [data scientists](https://code.visualstudio.com/docs/python/data-science-tutorial), [researchers](https://code.visualstudio.com/docs/python/jupyter-support), [developers](https://code.visualstudio.com/docs/python/python-tutorial), and journalists to analyze data and create reproducible research.

Examples of data journalism projects that could be developed using VS Code include:

* Jupyter notebooks for investigating public records
* Interactive data exploration and analysis
* Automated data processing pipelines
* Version-controlled research projects
* Collaborative data investigations using Git integration

You can find thousands of Python projects on [GitHub](https://github.com/search?q=language%3APython+data+analysis&type=Repositories) that use VS Code for development, including projects by [The New York Times](https://github.com/nytimes), [FiveThirtyEight](https://github.com/fivethirtyeight), [BuzzFeed News](https://github.com/BuzzFeedNews), and many others.

There are several ways to set up Python development in VS Code. This tutorial uses [uv](https://docs.astral.sh/uv/), a fast and modern Python package manager that makes dependency management simple and reliable. We'll walk you through installing VS Code, Python, uv, and all the tools you need for data analysis.

```{note}
We recommend uv for all users because it automatically manages Python installations and virtual environments, preventing common setup issues. Advanced users familiar with other tools (conda, pipenv, etc.) can adapt the examples, but following the uv approach will give you the smoothest experience.
```

## Install Visual Studio Code

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/VqCgcpAypFQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

The first step is to visit [Visual Studio Code's homepage](https://code.visualstudio.com/) in your web browser.

![VS Code homepage](/_static/vscode-homepage.png)

Click the "Download for [Your Operating System]" button. The website should automatically detect your operating system and show the appropriate download.

The installation file will download to your computer. Find the file in your downloads directory and double-click it to begin the installation process. Follow the instructions presented by the installation wizard, sticking to the default options.

```{warning}
On macOS, you may need to drag VS Code to your Applications folder after downloading. On Windows, the installer will handle everything for you. On Linux, you may need to install via your package manager or using the downloaded .deb/.rpm file.
```

## Install Python Extension

Once VS Code is installed, open it and you'll see the Welcome screen. We need to install the Python extension to get the best Python development experience.

![VS Code welcome screen](/_static/vscode-welcome.png)

1. Click on the Extensions icon in the left sidebar (it looks like four squares)
2. Search for "Python" in the extensions marketplace
3. Find the official Python extension by Microsoft (it should be the first result)
4. Click "Install"

![Python extension](/_static/python-extension.png)

This extension provides:
- IntelliSense (code completion and suggestions)
- Debugging support
- Code formatting and linting
- Jupyter notebook support
- Interactive Python (REPL) support

## Install Jupyter Extension

Since we'll be working with Jupyter notebooks, also install the Jupyter extension:

1. In the Extensions panel, search for "Jupyter"
2. Find the official Jupyter extension by Microsoft
3. Click "Install"

![Jupyter extension](/_static/jupyter-extension.png)

This extension enables:
- Full Jupyter notebook (.ipynb) support directly in VS Code
- Interactive Python cells in .py files
- Variable explorer
- Data viewer for pandas DataFrames
- Notebook diffing and merge capabilities

## Install uv (Python Package Manager)

Before setting up Python, we'll install uv, which will handle Python installation and package management for us. This approach ensures you get the latest Python version and eliminates common environment issues.

Open your terminal or command prompt and run the appropriate command for your operating system:

**On macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, restart your terminal or command prompt to ensure uv is available.

**Verify installation:**
```bash
uv --version
```

You should see the uv version number, confirming it's installed correctly.

## Set Up Your Project with uv

Now we'll create a new Python project and install all required packages. uv will automatically download and set up the correct Python version for you.

1. **Create your project directory:**
```bash
uv init first-python-notebook
cd first-python-notebook
```

2. **Install required packages:**
```bash
uv add pandas matplotlib seaborn jupyter altair
```

This command will:
- Download and install Python 3.12+ if needed
- Create a virtual environment automatically
- Install all required packages for data analysis
- Create a `pyproject.toml` file to track dependencies

The installation may take a few minutes the first time as uv downloads Python and packages.

## Verify Your Setup

Let's verify everything is working by testing Python and our installed packages:

1. **Open VS Code in your project:**

Launch VS Code and then open the first-python-notebook directory, or from the command line in that directory:

```bash
code .
```

2. **Create a test file:** Press `Ctrl+N` (or `Cmd+N` on Mac) to create a new file
3. **Save it as `test.py`:** Press `Ctrl+S` (or `Cmd+S`) and name it `test.py`
4. **Add test code:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import sys

print("🎉 All packages imported successfully!")
print(f"Python version: {sys.version}")
print(f"pandas version: {pd.__version__}")
print(f"altair version: {alt.__version__}")
```

5. **Run the file:** Right-click in the editor and select "Run Python File in Terminal"

You should see success messages and version numbers printed in the integrated terminal at the bottom of the screen.

```{tip}
If you see import errors, make sure VS Code has selected the correct Python interpreter (see the next section on environment selection).
```

## Your First Interactive Session

VS Code provides excellent support for working with Python and Jupyter notebooks. 

### Python Interactive Window

1. Create a new file and save it as `analysis.py` in your project directory
2. Add the following code:

```python
# %%
print("This is my first interactive cell")
x = 2 + 2
print(f"2 + 2 = {x}")
```

3. Click "Run Cell" above the `# %%` comment

This will open an Interactive Window where you can see the output, providing an interactive development experience integrated into VS Code.

### Jupyter Notebooks in VS Code

You can also create traditional Jupyter notebooks:

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
2. Type "Jupyter: Create New Jupyter Notebook"
3. Press Enter

This creates a new `.ipynb` notebook file where you can add cells and run them interactively. Save it and call it `notebook.ipynb`.

VS Code provides the full notebook experience including:
- Rich output display (plots, tables, HTML)
- Variable explorer
- Kernel management
- Cell execution controls
- Markdown and code cells

## Selecting the Right Python Environment

After installing packages, it's crucial to ensure VS Code uses the correct Python environment. This is especially important if you have multiple Python installations.

### For Python Files (.py)

When working with Python files, VS Code needs to know which Python interpreter to use. If you have `uv` installed, it will do this automatically.

### For Jupyter Notebooks (.ipynb)

Notebooks use "kernels" (similar to interpreters) to run code. When you start a new notebook, you can select a new kernel. You should be able to pick "Python Environments" and then the first choice should be `first-python-notebook`. Click on that.

Now you're ready to start learning Python for data analysis! The next chapter will introduce you to working with Jupyter notebooks in VS Code.
