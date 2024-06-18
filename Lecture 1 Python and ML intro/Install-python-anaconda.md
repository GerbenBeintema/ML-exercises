# Python installation instructions for use in 5SC28 ML for S&C

Python is a free and open-source alternative to MATLAB. It is the most popular language for deep learning applications. We will be using Python during the coming exercises. 

For these exercises, you will be using python with some extensions for streamlined array data handling (e.g `numpy`), visualization (e.g. `matplotlib`), machine learning (`sklearn`) and of course, deep learning (`PyTorch`).

Furthermore, the exercises will be provided as jupyter notebooks which allow for inline plotting and markdown formatting. 

## Quick-start

The easiest way to start with python programming is to use the notebook system provided by Google Colab which includes the `PyTorch` installation by default. This does require a Google Account and a stable internet connection. 

 1. Open Google Colab via https://colab.research.google.com/
 2. Login in to your Google account. 
 3. Upload the desired notebook.
 4. To save your work either save it to your Google drive or download it as a `.ipynb`.

However, some visualizations, datasets, and the design project are not be compatible with this interface, hence we recommend the local installation.

## Local installation (recommended)

Most of the required extensions are already included in the popular python package manager Anaconda (`PyTorch` is missing from this distribution and needs to be installed manually). If anything goes wrong, or you have any question about the installation feel free to contact Gerben. 

 1. Install Anaconda. (skip this step if you already have a version of anaconda)
    * Download (~450 MB) the anaconda python installer via [Download page](https://www.anaconda.com/products/individual) 
    * Install by following the instructions after opening the installer.
    * see: [problemsolvingwithpython](https://problemsolvingwithpython.com/01-Orientation/01.03-Installing-Anaconda-on-Windows/) for detailed instructions
 2. Setup virtual environment with Pytorch
    * Either open the anaconda navigator and launch the `CMD.exe Prompt` or `Powershell Prompt` or launch anaconda prompt by searching "anaconda prompt" in the start menu
    * create a virtual environment using a command like 
      * `conda create --name ml4sc python=x.x anaconda` where `x.x` is the python version you desire. In this course you can use python 3.8 up to 3.11 and you might consider MATLAB compatible (https://www.mathworks.com/support/requirements/python-compatibility.html).
    * Either type `conda activate ml4sc` to activate the environment or close the Prompt and activate the ml4sc environment by using the dropdown menu in the top left of the anaconda navigator
    * Install pytorch using the instruction on https://pytorch.org/get-started/locally/. 
    * type `conda install -c anaconda git` (needed to install modules from github such as the design environment)
 3. Opening a notebook.
    * Open the anaconda navigator
    * Activate the `ml4sc` environment if needed. 
    * Launch the Jupyter Notebook or Jupyter lab
    * Navigate to the desired Notebook and open. 
      * You can also launch the Notebook sever in a specific directory by using `Powershell Prompt` and the `ls` and `cd` commands
      * You might also need to type `conda activate ml4sc`.
      * If you are in the desired directory you can type `jupyter notebook` or `jupyter-lab`.

## What's next

After the installation one should open the `Quickstart-Tutorial.ipynb` notebook and thoughtfully go through the examples. Afterwards you can start with the exercises. 
