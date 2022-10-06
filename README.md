# Accelerate Your Coding with PyCharm and Visual Studio Code

### Sample code/scripts/notebooks for an "Introduction to Pycharm/VS Code" workshop

This repository contains a couple of simple scripts.
 - The `01_pandas.py` script loads and displays a sample dataset commonly used in Machine Learning.
 - The `02_faces.py` script loads a bunch of face images (AT&T employees from the early 1990s) and creates an *Average Face*.

The code included in this repository has some problems. We will use the IDE as much as possible to detect, debug and fix these problems.
Along the way we'll look at how the IDEs might help us in:

 - Isolating our work by environments.
 - Breaking functionality down into reusable functions.
 - Testing any functions we write.
 - Squashing bugs using a Debugger.
 - (If we must have notebooks), keeping the notebook code to a minimum.
 - Following pep8 recommendations and fixing common anti-patterns.
 - Profiling and optimizing our code.
 - Using remote interpreters when our laptop just won't do the job.

### The Plan

Here is a rough outline we will follow:

 - Run some simple scripts in a local `conda` environment.
 - Specify dependencies for our project.
 - Refactor our script into a reusable module.
 - Write tests for the module. Some of these will fail.
 - Refactor our module to satisfy all tests.
 - Reformat our code to adhere to professional standards.
 - Write a helper jupyter notebook for visualization.
 - Run our scripts/tests remotely on `adroit-vis.princeton.edu` against *real* data.
 - Run our jupyter notebook remotely on `adroit-vis.princeton.edu` against *real* data.


#### Details

**Make sure that you use `python=3.8` when creating the `conda` environment.** Later versions have some issues with some dependencies, especially on Apple Silicon.

Here are some links and fragments of code/commands that will be helpful to copy-paste during the workshop:

A complete list of requirements we will be using:

```
jupyter
matplotlib
numpy
pandas
pytest
scikit-learn
```

A function that calculates the *average face* given a folder of face images:

```
def average_face(folder):
    import glob

    images = []
    for file in glob.glob(f'{folder}/*.jpg'):
        images.append(imread(file).flatten())

    X = np.vstack(images)
    return np.mean(X, axis=0).reshape((64, 64))
```

The following commands are taken from [Jupyter on HPC Clusters](https://researchcomputing.princeton.edu/support/knowledge-base/jupyter)

```
module load anaconda3/2022.5
jupyter-notebook --no-browser --port=8889 --ip=127.0.0.1
```

Note that the actual assigned port may not be `8889`!

Opening up an *ssh-tunnel* from our local computer to `adroit-vis`:

```
ssh -N -f -L localhost:8889:localhost:8889 <YourNetID>@adroit-vis.princeton.edu
```

