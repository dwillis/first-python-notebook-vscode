# Export

<div class="responsive-iframe-container">
    <iframe cThis will create a CSV file without the index with semicolons as the separator between values.

## Share Your Work on GitHub

Now that you've completed your analysis and exported your results, let's share your work on GitHub so others can see what you've accomplished and you can showcase your data journalism skills.

### Create a GitHub Repository

1. **Go to [GitHub.com](https://github.com)** and sign in to your account
2. **Click the "+" icon** in the top-right corner and select "New repository"
3. **Name your repository** `first-python-notebook`
4. **Add a description** like "My first data analysis project using Python and pandas"
5. **Keep it public** so others can see your work
6. **Don't initialize** with README, .gitignore, or license (we'll add these ourselves)
7. **Click "Create repository"**

### Connect Your Local Project to GitHub

Now we'll connect your local VS Code project to the GitHub repository using VS Code's integrated terminal.

1. **Open the terminal** in VS Code (`View > Terminal` or `Ctrl+`` `)

2. **Initialize git** (if not already done):
```bash
git init
```

3. **Add your GitHub repository as the remote origin** (replace `YOUR_USERNAME` with your actual GitHub username):
```bash
git remote add origin https://github.com/YOUR_USERNAME/first-python-notebook.git
```

### Add and Commit Your Files

Let's add all your work to git and commit it:

1. **Check what files you have**:
```bash
git status
```

2. **Add all your files** to git:
```bash
git add .
```

3. **Commit your work** with a descriptive message:
```bash
git commit -m "Initial commit: helicopter accident rate analysis complete"
```

4. **Push to GitHub**:
```bash
git push -u origin main
```

```{tip}
If you get an error about authentication, you may need to set up a personal access token. GitHub has excellent documentation on [creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for command line use.
```

### Create a README

Let's add a README file to document your project:

1. **Create a new file** called `README.md` in VS Code
2. **Add project documentation**:

```markdown
# First Python Notebook

My first data analysis project analyzing helicopter accident rates using Python, pandas, and VS Code.

## Project Overview

This project analyzes helicopter accident data from the NTSB and flight hour data from the FAA to calculate accident rates per 100,000 flight hours for different helicopter models.

## Files

- `accident-rate-ranking.csv` - Final analysis results showing accident rates by helicopter model
- Analysis notebooks and scripts used for data processing and visualization

## Key Findings

[Add a few sentences about what you discovered in your analysis]

## Tools Used

- Python
- pandas for data manipulation
- matplotlib and seaborn for visualization
- VS Code for development
- uv for package management

## Data Sources

- NTSB helicopter accident data
- FAA General Aviation and Part 135 Activity Survey
```

3. **Save the file**, then add, commit, and push it:
```bash
git add README.md
git commit -m "Add project README with documentation"
git push
```

### View Your Published Work

Go back to your GitHub repository page and refresh it. You should now see:
- All your Python files and notebooks
- Your exported CSV data
- A professional README describing your project

And with that, you've completed "First Python Notebook." If you have any questions or critiques, you can get involved on [our GitHub repository](https://github.com/palewire/first-python-notebook), where all of the code that powers this site is available as open source.s="responsive-iframe" src="https://www.youtube.com/embed/m9LTVLETSeo?si=XqHQp8XQ91hP90wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Saving the dataframes you've created to your computer requires one final pandas method. It's [`to_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html), an exporting companion to `read_csv`. Append it to any dataframe and provide a filepath. That's all it takes.

```python
# %%
# Setup data for export examples
import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list['latimes_make_and_model'] = accident_list['latimes_make_and_model'].str.upper()
accident_counts = accident_list.groupby(["latimes_make", "latimes_make_and_model"]).size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
survey['latimes_make_and_model'] = survey['latimes_make_and_model'].str.upper()
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
merged_list['per_hour'] = merged_list.accidents / merged_list.total_hours
merged_list['per_100k_hours'] = (merged_list.accidents / merged_list.total_hours) * 100_000
print("Data prepared for export")
```

```python
# %%
merged_list.to_csv("accident-rate-ranking.csv")
print("Data exported to accident-rate-ranking.csv")
```

```{code-cell}
:tags: [hide-cell]

import pandas as pd
accident_list = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/ntsb-accidents.csv")
accident_list['latimes_make_and_model'] = accident_list['latimes_make_and_model'].str.upper()
accident_counts = accident_list.groupby(["latimes_make", "latimes_make_and_model"]).size().reset_index().rename(columns={0: "accidents"})
survey = pd.read_csv("https://raw.githubusercontent.com/palewire/first-python-notebook/main/docs/src/_static/faa-survey.csv")
survey['latimes_make_and_model'] = survey['latimes_make_and_model'].str.upper()
merged_list = pd.merge(accident_counts, survey, on="latimes_make_and_model")
merged_list['per_hour'] = merged_list.accidents / merged_list.total_hours
merged_list['per_100k_hours'] = (merged_list.accidents / merged_list.total_hours) * 100_000
```

```{code-cell}
merged_list.to_csv("accident-rate-ranking.csv")
```

The file it creates can be imported into other programs for reuse, including the data visualization tools many newsrooms rely on to publish graphics. For instance, the file we've exported above could be used to quickly draft a chart with [Datawrapper](https://datawrapper.de/), like this one:

<iframe title="Helicopter accident rates" aria-label="Split Bars" id="datawrapper-chart-6gTy3" src="https://datawrapper.dwcdn.net/6gTy3/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="452" data-external="1"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(e){if(void 0!==e.data["datawrapper-height"]){var t=document.querySelectorAll("iframe");for(var a in e.data["datawrapper-height"])for(var r=0;r<t.length;r++){if(t[r].contentWindow===e.source)t[r].style.height=e.data["datawrapper-height"][a]+"px"}}}))}();
</script>

```{note}
Interested in learning more about how to publish data online? Check out ["First Visual Story,"](https://palewi.re/docs/first-visual-story/) a tutorial that will show you how journalists at America’s top news organizations escape rigid content-management systems to publish custom interactive graphics on deadline.
```


The `to_csv()` method accepts several optional arguments. The most important one is the filename input, which is used to specify the path and name of the file that will be created. The `index=False` keyword argument tells pandas to exclude the index column of the DataFrame. You can also specify the separator by passing the `sep` parameter.

```python
# %%
merged_list.to_csv("accident-rate-ranking.csv", index=False, sep=";")
print("Data exported with custom options (no index, semicolon separator)")
```

This will create a CSV file without the index with semicolons as the separator between values.

And with that, you've completed “First Python Notebook.” If you have any questions or critiques, you can get involved on [our GitHub repository](https://github.com/palewire/first-python-notebook), where all of the code that powers this site is available as open source.
