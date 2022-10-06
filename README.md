# Accelerate Your Coding with PyCharm and Visual Studio Code

### The Plan

The code included in this repository has some problems. We will use the IDE as much as possible to detect, debug and fix these problems.
Along the way we'll look at how the IDEs might help us in:

 - Run some simple scripts in a local `conda` environment.
 - Specify dependencies for our project.
 - Refactor our script into a reusable module.
 - Write tests for the module. Some of these will fail.
 - Refactor our module to satisfy all tests.
 - Write a helper jupyter notebook for visualization.
 - Refactor/format our code to adhere to professional standards. (`pep8`)
 - Profile code for potential speedups.
 - Run our scripts/tests remotely on `adroit-vis.princeton.edu` against *real* data, without leaving the IDE.
 - Run our jupyter notebook remotely on `adroit-vis.princeton.edu` against *real* data, without leaving the IDE.


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

The remote server we will use is `adroit-vis.princeton.edu`. The data is located at `/scratch/network/vineetb/data`.

The following commands are taken from the excellent resource [Jupyter on HPC Clusters](https://researchcomputing.princeton.edu/support/knowledge-base/jupyter).
Another excellent resource for VS-Code is [Visual Studio Code and Remote Code Development](https://researchcomputing.princeton.edu/visual-studio-code-and-remote-code-development).

```
module load anaconda3/2022.5
jupyter-notebook --no-browser --port=8889 --ip=127.0.0.1
```

Note that the actual assigned port may not be `8889`!

Opening up an *ssh-tunnel* from our local computer to `adroit-vis`:

```
ssh -N -f -L localhost:8889:localhost:8889 <YourNetID>@adroit-vis.princeton.edu
```

