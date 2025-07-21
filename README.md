# TripleTen Projects

In this project we are learing how to configure a local environment using Anaconda, Github and Render, using Visual Studio Code as main IDE to program the project, the steps describes how to configure the environment.

## Environment Configuration 

`conda env create --file environment.yml`

> **Note:** In my case I had to run this command before activation the environment:

`source activate base`

then

`conda install -n vehicles_env nbformat`
`conda activate vehicles_env`

## PROJECT
The following exercise is related to a car study, so we are going to do some graphics using `plotly` and `streamlit` to export the project as web application that will be rendered with `Render`.