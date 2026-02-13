import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.md(
        """
        # Welcome to Marimo! 🎉

        This is a simple example notebook to get you started with data science using UV and Marimo.

        Marimo is a reactive Python notebook that runs as an interactive app.
        """
    )
    return


@app.cell
def __():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    return np, pd, plt, sns


@app.cell
def __(mo):
    mo.md(
        """
        ## Let's create some sample data

        Below we'll create a simple dataset and visualize it.
        """
    )
    return


@app.cell
def __(np, pd):
    # Create sample data
    data = pd.DataFrame({
        'x': np.linspace(0, 10, 100),
        'y': np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100)
    })
    data
    return (data,)


@app.cell
def __(data, mo, plt, sns):
    # Create a plot
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=data, x='x', y='y', ax=ax)
    ax.set_title('Sample Data Visualization')
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')
    plt.tight_layout()
    
    mo.md(f"""
    ## Visualization
    
    Here's a scatter plot of our sample data:
    
    {mo.as_html(plt.gcf())}
    
    **Data shape:** {data.shape[0]} rows × {data.shape[1]} columns
    """)
    return ax, fig


@app.cell
def __(mo):
    mo.md(
        """
        ## Next Steps

        Try modifying the code above to:
        - Change the data generation parameters
        - Add more columns to the dataframe
        - Create different types of plots
        - Import and analyze your own data

        Marimo will automatically re-run dependent cells when you make changes!
        """
    )
    return


if __name__ == "__main__":
    app.run()
