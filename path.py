from gcodeparser import GcodeParser
import math

class path_planner():
    def __init__(self, file_path, accuracy, acc_limit, dec_limit, speed_limit):
        '''Input: 
        file: gcode file path
        accuracy: minimum step size of the arm
        acc_limit: maximum acceleration of the arm
        dec_limit: maximum deceleration of the arm
        speed_limit: maximum speed of the arm 
        '''
        self.x, self.y, self.z, self.f = 0, 0, 0, 0
        self.gcode = read_gcode(file_path)
        
    
    def read_gcode(self, file):
        parser = GcodeParser(file_path)
        with open('setup.gcode', 'r') as f:
            gcode = f.read()

        lines = GcodeParser(gcode).lines
        return lines
    
    
    def generate(self):
        ''' Go line by line of the gcode file and generate the path
        '''
        for line in gcode:
            if line.command_str == 'G28':
                self.G28()
            elif line.command_str == 'G0':
                self.G0()
            elif line.command_str == 'G1':
                self.G1()
            else:
                print('Command not recognized: {}'.format(line.command_str))
    
    
    def G28(self):
        pass
    
    def G0(self):
        pass
    
    def G1(self):
        pass

if "__main__" == __name__:
    parser()