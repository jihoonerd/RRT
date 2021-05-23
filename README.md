# RRT

Implementation of Rapidly-exploring Random Tree(RRT)

## Vanilla RRT Demo

|Path Finding|Full Trajectory|
|---|---|
|![RRT_GIF](asset/rrt.gif)|![RRT_PATH](asset/rrt_path.jpg)|

## Installation

```bash
$ pip install -r requirements.txt
```

## How to use

```python
$ python main.py --help
usage: main.py [-h] [--map MAP] [--stepsize STEPSIZE]

optional arguments:
  -h, --help           show this help message and exit
  --map MAP            path to map file
  --stepsize STEPSIZE  step size
```

Example
```python
$ python main.py --map map.png --stepsize 40
```

When scren pops up, your first clicked position will be a starting point, and second clicked position will be a target point. Path finding process will launch automatically.

## TODO

* RRT*