import marimo

__generated_with = "0.19.11"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Welcome to Marimo! 🎉

    This is a simple example notebook to get you started with data science using UV and Marimo.

    Marimo is a reactive Python notebook that runs as an interactive app.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import lets_plot as lp

    return lp, np, pd, px


@app.cell
def _(mo):
    mo.md("""
    ## Let's create some sample data

    Below we'll create a simple dataset and visualize it.
    """)
    return


@app.cell
def _(np, pd):
    # Create sample data
    data = pd.DataFrame({
        'x': np.linspace(0, 10, 100),
        'y': np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100)
    })
    data
    return (data,)


@app.cell
def _(data, px):
    px.scatter(data, x='x', y='y')
    return


@app.cell
def _(data, lp):
    lp.ggplot(data, lp.aes(x='x', y='y')) + lp.geom_point()
    return


@app.cell
def _(mo):
    mo.md("""
    ## Next Steps

    Try modifying the code above to:
    - Change the data generation parameters
    - Add more columns to the dataframe
    - Create different types of plots
    - Import and analyze your own data

    Marimo will automatically re-run dependent cells when you make changes!
    """)
    return


if __name__ == "__main__":
    app.run()
