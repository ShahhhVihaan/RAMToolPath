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
        self.x, self.y, self.z, self.f, self.e = 0, 0, 0, 0, 0
        self.file_path = file_path
        self.gcode = self.read_gcode(file_path)
        
    
    def read_gcode(self, file):
        parser = GcodeParser(file)
        with open(file, 'r') as f:
            gcode = f.read()

        lines = GcodeParser(gcode).lines
        return lines
    
    
    def generate(self):
        ''' Calls the appropriate function based on the gcode command
            Example: 'G0' -> self.G0(line)
        '''
        for line in self.gcode:
            try:
                command = getattr(self, line.command_str)
                yield command(line)
            except AttributeError:
                print('Command not recognized: {}'.format(line.command_str))

    
    def line_get_params(self, line):
        x = line.get_param('X') if line.get_param('X') is not None else self.x
        y = line.get_param('Y') if line.get_param('Y') is not None else self.y
        z = line.get_param('Z') if line.get_param('Z') is not None else self.z
        f = line.get_param('F') if line.get_param('F') is not None else self.f
        e = line.get_param('E') if line.get_param('E') is not None else self.e

        return x, y
            
    def G28(self, line):
        pass
    
    def G0(self, line):
        t = self.line_get_params(line)
        return t[0], t[1]
    
    def G1(self, line):
        t = self.line_get_params(line)
        return t[0], t[1]


if __name__ == "__main__":
    a = Planner('sample_gcode/setup.gcode')
    
    for i, j in a.generate():
        print(i, j)