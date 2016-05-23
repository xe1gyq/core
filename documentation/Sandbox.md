# Sandbox

## xPlotLy

> Plotly is an online analytics and data visualization tool, headquartered in Montreal, Quebec. Plotly provides online graphing, analytics, and stats tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, and REST. Wikipedia. [Wikipedia](https://en.wikipedia.org/wiki/Plotly)

[PlotLy Homepage](https://plot.ly/)


```sh
    $ python core/xplotly.py
```

```Python
    from core.xplotly import xPlotLy
    
    xPlotly = xPlotLy("Core PlotLy Random")
    counter = 0
    while True:
        xPlotly.graph(counter, random.random())
        counter += 1
        time.sleep(0.5)
```
