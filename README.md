# terminalplot
![Console plot](/plot.png)

## Installation
    pip install terminalplot

## Usage
### Plotting a graph
```python
from terminalplot import plot
x = range(100)
y = [i**2 for i in x]
plot(x, y)
```

### Get size of current terminal window
```python
from terminalplot import get_terminal_size
get_terminal_size()
```
