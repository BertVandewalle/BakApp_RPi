from math import sqrt
from qt_core import *
import numpy as np
import scipy.optimize as sp


class GoalController(QWidget):
    R = 0.03325/2
    v = 0
    theta = 0
    ypos = 0
    teamColor = 'green' 
    def __init__(self):
        super().__init__()
        self.serial = QtSerialPort.QSerialPort(
                    'COM8',
                    baudRate=QtSerialPort.QSerialPort.Baud9600,
                    readyRead=self.receiveMsg)
        if not self.serial.isOpen():
            self.serial.open(QIODevice.ReadWrite)
        self.goalScored = QPushButton(self)

    def receiveMsg(self):
        if self.serial.size() > 119:
            start_of_msg = self.serial.read(1)
            if start_of_msg == bytes.fromhex("F0"):
                lasers =[]
                self.goal_id = int.from_bytes(self.serial.read(1),"little")
                if self.goal_id == 1:
                    self.teamColor = 'green'
                else: 
                    self.teamColor = 'red'
                n_hits_bytes = self.serial.read(1)
                n_hits = int.from_bytes(n_hits_bytes,"little")
                for i in range(n_hits):
                    laser_id = int.from_bytes(self.serial.read(1),"little")
                    t1_bytes = self.serial.read(4)
                    t1 = int.from_bytes(t1_bytes,"little")
                    t2_bytes =self.serial.read(4)
                    t2 = int.from_bytes(t2_bytes,"little")
                    lasers.append(Laser(laser_id,t1,t2))

            
                if lasers != None:
                    self.CalcGoal(lasers)

                self.serial.flush()

    def GoalFunc(self,variables,*args):
        R = args[0]
        t1 = args[1]
        t2 = args[2]
        t3 = args[3]
        t4 = args[4]
        rl1 = args[5]
        rl2 = args[6]

        (vx,vy,xc1,yc1,xc2,yc2,xc3,yc3,xc4,yc4) = variables

        eqn_1 = xc2-xc1-vx*(t2-t1)
        eqn_2 = yc2-yc1-vy*(t2-t1)
        eqn_3 = xc3-xc1-vx*(t3-t1)
        eqn_4 = yc3-yc1-vy*(t3-t1)
        eqn_5 = xc4-xc1-vx*(t4-t1)
        eqn_6 = yc4-yc1-vy*(t4-t1)
        eqn_7 = (xc1-rl1[0])**2+ (yc1-rl1[1])**2 - R**2
        eqn_8 = (xc2-rl2[0])**2+ (yc2-rl2[1])**2 - R**2
        eqn_9 = (xc3-rl1[0])**2+ (yc3-rl1[1])**2 - R**2
        eqn_10 = (xc4-rl2[0])**2+ (yc4-rl2[1])**2 - R**2

        return [eqn_1,eqn_2,eqn_3,eqn_4,eqn_5,eqn_6,eqn_7,eqn_8,eqn_9,eqn_10]

    def CalcGoal(self,hitLasers):
        n = len(hitLasers)
        solutions = []
        for i in range(n):
            for j in range(n):
                if i!=j:
                    variables = (np.array([5,0]),
                                (hitLasers[j].pos+hitLasers[i].pos)/2+np.array([-self.R,0]),
                                (hitLasers[j].pos+hitLasers[i].pos)/2+np.array([-self.R,0]),
                                (hitLasers[j].pos+hitLasers[i].pos)/2+np.array([self.R,0]),
                                (hitLasers[j].pos+hitLasers[i].pos)/2+np.array([self.R,0]))

                    result = sp.fsolve(self.GoalFunc,(np.array([5,0]),
                                (hitLasers[j].pos+hitLasers[i].pos)/2+np.array([-self.R,0]),
                                (hitLasers[j].pos+hitLasers[i].pos)/2+np.array([-self.R,0]),
                                (hitLasers[j].pos+hitLasers[i].pos)/2+np.array([self.R,0]),
                                (hitLasers[j].pos+hitLasers[i].pos)/2+np.array([self.R,0])),
                                        args=(self.R,hitLasers[i].t1*1e-7,
                                            hitLasers[j].t1*1e-7,
                                            hitLasers[i].t2*1e-7,
                                            hitLasers[j].t2*1e-7,
                                            hitLasers[i].pos,
                                            hitLasers[j].pos),
                                            xtol=1.49012e-11)

                    solutions.append(result)
                    # v = np.sqrt(result[0]**2+result[1]**2)
                    # theta = np.arctan(result[1]/result[0])*180/np.pi
                    # solutions.append(np.array([v,theta]))
        solution_avg = [0]*len(solutions[0])
        for i in range(n):
            for j in range(len(solutions)):
                solution_avg[j] += solutions[i][j]

        solution_avg =[x/n for x in solution_avg]
        self.v = sqrt(solution_avg[0]**2+solution_avg[1]**2)* 3.6
        self.theta = np.arctan(np.arctan(solution_avg[1]/solution_avg[0]))
        self.ypos = solutions[0][3] + solutions[0][1]/solutions[0][0]*(self.R-0.015-solutions[0][2])
        self.ypos *=1000 
        print(f"v = {self.v} km/h\ttheta = {self.theta*180/np.pi} deg\n")
        self.goalScored.clicked.emit()
                
                
class Laser():
    def __init__(self,id,t1,t2):
        self.id = id
        self.t1 = t1
        self.t2 = t2

    @property
    def pos(self):
        return np.array([0.0,(self.id-6)*5*0.0024])