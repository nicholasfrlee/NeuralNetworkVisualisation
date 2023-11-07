## README.md

This is a repository dedicated to try to visualise an instance of a neural network, based on the different layer sizes and activation functions in between the layers. The code is based off the Manim Python library.

Demo photos can be found under images/EXAMPLE_SCENE_X.jpg

The focus of this point in the repository is the 2 files neural_net.py and visualise.py, whereby neural_net.py is a simple file to generate an instance of a neural network and train it on the MNIST fashion dataset. visualise.py is an attempt to visualise the layers of the neural network specified in neural_net.py

**How to run the code in this repository**

To run the code in this repository, you will need to have the following installed:

* Python 3
* Conda
* Manim

**Installing Manim**

To install Manim on conda, run the following comman in the terminal:
`conda install -c conda-forge manim`

To run the script, run the following command in the terminal:
The flag for low rendering is -pql
The flag for high quality rendering is -pqk

For example
`manim -pql visualise.py -o [OUTPUT_FILE.mp4]`