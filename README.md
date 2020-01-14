# Do-a-thon for OpenMod January 2020 in Berlin

Very often data is conveyed to the public or shared with other researchers in the
form of graphs. In the case of large datasets there is often many ways to visualize the data, which
ultimately depend on the end-user interests or preferences. Plotly Dash is very handy for building
data visualization apps with custom user interfaces in pure Python. Since Dash apps are viewed in
the web browser, Dash is inherently cross-platform and mobile ready. The apps can be deployed
locally or to servers. We will build a simple Dash app together.

## Requirements

* python 3.6 or higher

## Getting started

1. Clone the repository locally
2. [Setup](https://oemof.readthedocs.io/en/latest/installation_and_setup.html#using-virtualenv-community-driven) a virtual environment.
3. Install the dependencies `pip install -r requirements.txt` or `conda env create --file=environment.yml`
4. run the app locally with `python app.py`, you can visualize it in your browser under 
`http://127.0.0.1:8050`
 
## Resources

- [Dash User Guide](https://dash.plot.ly/) contains the description of all dash components (core, html, datatable, daq) as well of examples and tutorials on how to use the Plotly dash functionalities

- [App example gallery](https://dash-gallery.plotly.host/Portal/) help you forsee what you can do with Plotly dash

## Tips

- in a python terminal type `help(dash_core_components.<name of your component>` to get the description of the component as well as its properties (you need to `import dash_core_components` beforehand)