# Module wordish
Function to reveal the math attributes from arbitrary text

# Quick start
## Setting up the environment

Using Anaconda, open the Anaconda Prompt and run the command:

````commandline
conda env creeate -n wordish -f env_file.yaml
````
Activate the environment using the command:
````commandline
conda activate wordish
````
Then, test the environmonet by running the main module using:
```python
python -m wordish.main --file items.json
```
In your favorite IDE choose the newly created python environment.

## Checking the code
In ```tasks.py``` different utility function are defined for code style, formatting, syntax and tests.

### Pycodestyle
In terminal window run pycodestyle using:
```python
invoke style
```
Correct the code according to the output.

### Pylint
In terminal window run pylint using:
```python
invoke lint
```
Correct the code according to the output.

### Unit tests
In terminal window run unit tests using:
```python
invoke unit-tests
```
(NB! The underscore becomes a dash when calling the function.)

Important to isolate each test to its input and output reference frame using mocking functionality.

Coverage should aim for 100%.

### Integration tests
In terminal window run integration tests using:

```python
invoke unit-tests
```
Coverage should aim for 100%.