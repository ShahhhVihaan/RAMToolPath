from gcodeparser import GcodeParser
import math

class Planner():
    def __init__(self, file_path, accuracy = 0, acc_limit = 0, dec_limit = 0, speed_limit = 0):
        '''Input: 
        file: gcode file path
        accuracy: minimum step size of the arm
        acc_limit: maximum acceleration of the arm
        dec_limit: maximum deceleration of the arm
        speed_limit: maximum speed of the arm 
        '''
        self.x, self.y, self.z, self.f = 0, 0, 0, 0
        self.file_path = file_path
        self.gcode = self.read_gcode(file_path)
        
    
    def read_gcode(self, file):
        parser = GcodeParser(file)
        with open(file, 'r') as f:
            gcode = f.read()

        lines = GcodeParser(gcode).lines
        return lines
    
    
    def generate(self):
        ''' Go line by line of the gcode file and generate the path
        '''
        for line in self.gcode:
            try:
                command = getattr(self, line.command_str)
                return command(line)
            except AttributeError:
                print('Command not recognized: {}'.format(line.command_str))

    
    def line_get_params(self, line):
        if line.get_param('X'):
            x = line.get_param('X')
        if line.get_param('Y'):
            y = line.get_param('Y')
        if line.get_param('Z'):
            z = line.get_param('Z')
        if line.get_param('F'):
            f = line.get_param('F')
        
        return x, y, z, f
        
    def not_found(self, line):
        return 'Command not recognized: {}'.format(line.command_str)
    
    def G28(self, line):
        pass
    
    def G0(self, line):
        new_x, new_y, new_z, new_f = self.line_get_params(line)
        return new_x, new_y
    
    def G1(self, line):
        new_x, new_y, new_z, new_f = self.line_get_params(line)
        return new_x, new_y

if "__main__" == __name__:
    parser()