## Streamlit app to explore HTS results for Library 2

This is a streamlit app to display screening results as an interactive heatmap. A ready-to-use version of this app is hosted on streamlit.

<a href='https://library2-heatmap.streamlit.app/'>Link to app!</a>


## Dependencies

To run code locally on a standard PC, we recommend <code>Windows 11</code>, miniconda <code>conda 24.7.1</code> and <code>python 3.12.12</code>. All required python dependencies are listed in requirements.txt.

## Install instructions

The code for the interactive heatmaps can be used either as a ready to use version hosted by streamlit via the provided links or can be run on a local machine.

To run the code on a local machine:

1.	Download the github repository (clone or download zip and extract).
2.	Create a python environment with miniconda or anaconda. Open the mini/anaconda prompt window and use following command.
```
conda create -n intenv python=3.12.12
```
3.	Activate your environment
```
conda activate intenv
```
4.	Navigate to the downloaded folder containing the program and the data.
```
cd C:\*paste the location on your computer of the folder you downloaded and extracted*\library2_interactive_heatmap-main
```
5.	Install all required dependencies using the provided requirements.txt file.
```
pip install -r requirements.txt
```
6.	Run the program which opens a browser window with the interactive heatmap.
```
streamlit run lib2_streamlit_app.py
```

Installing and compiling on a standard computer should take less than 30 minutes.

## Demo

### Output in browser window

![lib2output](/demo/lib2output.png)

### Zoom using magnifying glass tool

![lib2zoom](/demo/lib2zoom.png)

### Output when square in heatmap is clicked

![lib2clicked](/demo/lib2clicked.png)

