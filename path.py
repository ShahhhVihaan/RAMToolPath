from gcodeparser import GcodeParser
import math
import re

class Planner():
    def __init__(self, file_path, accuracy = 0, acc_limit = 0, dec_limit = 0, speed_limit = 0):
        '''
        Input: 
        file: gcode file path
        accuracy: minimum step size of the arm
        acc_limit: maximum acceleration of the arm
        dec_limit: maximum deceleration of the arm
        speed_limit: maximum speed of the arm 
        '''
        self.x, self.y, self.z, self.f, self.e, self.comment = 0, 0, 0, 0, 0, ""
        self.file_path = file_path
        self.gcode = self.read_gcode()
        
    
    def read_gcode(self):
        parser = GcodeParser(self.file_path)
        with open(self.file_path, 'r') as f:
            gcode = f.read()

        lines = GcodeParser(gcode).lines
        return lines
    
    
    def generate(self):
        ''' 
        Calls the appropriate function based on the gcode command
        Example: 'G0' -> self.G0(line)
        '''
        for line in self.gcode:
            try:
                command = getattr(self, line.command_str)
                yield command(line)
            except AttributeError:
                # print('Command not recognized: {}'.format(line.command_str))
                pass

    
    def line_get_params(self, line):
        '''
        New x, y, z, f, e values are set to the current values if the line does not have a value for that parameter
        '''
        self.x = line.get_param('X') if line.get_param('X') is not None else self.x
        self.y = line.get_param('Y') if line.get_param('Y') is not None else self.y
        self.z = line.get_param('Z') if line.get_param('Z') is not None else self.z
        self.f = line.get_param('F') if line.get_param('F') is not None else self.f
        self.e = line.get_param('E') if line.get_param('E') is not None else self.e
        # self.comment = line.comment if line.comment is not None else self.comment
        return self.x, self.y, self.z, line.command_str
            
    def G28(self, line):
        pass
    
    def G0(self, line):
        t = self.line_get_params(line)
        # return the x, y, z coordinates and command
        return t[0], t[1], t[2], t[3]
    
    def G1(self, line):
        t = self.line_get_params(line)
        # return the x, y, z coordinates and command
        return t[0], t[1], t[2], t[3]


if __name__ == "__main__":
    path = Planner('sample_gcode/test_big_box.gcode')
    
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    for coord in path.generate():
        x, y, z, w = coord
        x = x - 5.2
        y = y - 5.2
        
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        
    print("min_x: {}, max_x: {}, min_y: {}, max_y: {}".format(min_x, max_x, min_y, max_y))