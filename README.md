# RAMToolPath
A G-code parser to generate trajectories for Robotic Arm FFF (Fused Filament Fabrication) part of the RAM (Robotic Additive Manufacturing) Suite.


## Dependencies

Install the dependencies with:

```bash
pip install -r requirements.txt
```
    
## Support

Support only available for G0 and G1 command coordinates. Full command support plus trajectory equations for RepRap firmware coming soon.


## Usage/Examples

```python
path = Planner("{gcode_file_path}")
path.generate()
    
for x, y, z, command in path.generate():
    print(x, y)
```


## Demo

[Video](https://drive.google.com/file/d/1mAAli1yfJo87GY5fJd7tMTUGNHNI2w3W/view?usp=sharing)
