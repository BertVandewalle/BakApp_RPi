import sys
from data_initializer import DataInitializer
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
from gui.widgets.timeline import TimeLine
from qt_core import *
import math

class GoalPage(QWidget):
    def __init__(self):
        super().__init__()

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self._teamColor = self.themes['app_color']['green']
        self._ballPos = 0
        self._theta = 0
        self._v = 0

    @property
    def teamColor(self):
        return self._teamColor
    @teamColor.setter
    def teamColor(self,value):
        self._teamColor = self.themes['app_color'][f"{value}"]

    def paintEvent(self,event):
        margin = 200
        w_goalline = self.width() - 2*margin
        h_goalline = w_goalline *15/172
        y_goalline = self.height()*0.67


        ball_size = w_goalline *33/172
        ball_center = QPoint(margin + w_goalline//2+ w_goalline*self._ballPos/172,y_goalline-h_goalline//2-ball_size//2)
        # ball_origin = QPoint(margin + w_goalline//2+self._ballPos/172-ball_size/2,
        #                 y_goalline-ball_size-h_goalline/2)


        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        self.drawGoalLine(h_goalline,y_goalline,margin,p)
        self.drawBall(ball_center,ball_size,p)
        self.drawDottedLine(ball_center,ball_size,p)
        end_point = self.drawArrow(ball_center,ball_size,p)
        self.drawText(margin,ball_size,y_goalline,p)
        p.end()

    def drawGoalLine(self,h,y,margin,p:QPainter):
        pen = QPen()
        pen.setWidth(h)
        pen.setColor(QColor(Qt.white))
        pen.setCapStyle(Qt.FlatCap)
        p.setPen(pen)
        p.drawLine(margin,y,self.width()-margin,y)

    def drawBall(self,center,size,p:QPainter):
        p.setPen(QPen(QColor(self.teamColor)))
        p.setBrush(QBrush(QColor(self.teamColor)))
        p.drawEllipse(center,size//2,size//2)

    def drawDottedLine(self,origin:QPoint,ball_size,p:QPainter):
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.white)
        pen.setStyle(Qt.DotLine)
        pen.setCapStyle(Qt.FlatCap)
        p.setPen(pen)
        p.drawLine(origin,origin-QPoint(0,ball_size))

    def drawArrow(self,origin:QPoint,ball_size,p:QPainter):
        length = ball_size
        gamma = 45*math.pi/180
        l_arrow = 5+0.1*length
        end_point = origin + QPoint(math.sin(self._theta)*length,-math.cos(self._theta)*length)
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.white)
        pen.setCapStyle(Qt.FlatCap)
        p.setPen(pen)
        p.drawLine(origin,end_point)
        p.drawLine(end_point,end_point +QPoint(math.sin(gamma-self._theta)*l_arrow,math.cos(gamma-self._theta)*l_arrow))
        p.drawLine(end_point,end_point +QPoint(math.sin(-gamma-self._theta)*l_arrow,math.cos(-gamma-self._theta)*l_arrow))
        return end_point

    def drawText(self,margin,ball_size,y_goalline, p:QPainter):
        p.setFont(QFont(self.settings['font']['family'],ball_size//2))
        p.drawText(QPoint(self.width()//2,y_goalline-ball_size*2),f"{self._v:.2f} km/h")
        p.drawText(QPoint(margin,y_goalline-ball_size*2),f"{self._theta*180/math.pi:.1f}°")

    def updateGoal(self,teamColor,v,theta,pos):
        teamColor=teamColor
        self._ballPos = pos
        self._theta = theta
        self._v = v
        self.repaint()




class Path(QGraphicsPathItem):
    def __init__(self, source: QPointF = None, destination: QPointF = None, *args, **kwargs):
        super(Path, self).__init__(*args, **kwargs)

        self._sourcePoint = source
        self._destinationPoint = destination

        self._arrow_height = 5
        self._arrow_width = 4

    def setSource(self, point: QPointF):
        self._sourcePoint = point

    def setDestination(self, point: QPointF):
        self._destinationPoint = point

    def directPath(self):
        path = QPainterPath(self._sourcePoint)
        path.lineTo(self._destinationPoint)
        return path

    def arrowCalc(self, start_point=None, end_point=None):  # calculates the point where the arrow should be drawn

        try:
            startPoint, endPoint = start_point, end_point

            if start_point is None:
                startPoint = self._sourcePoint

            if endPoint is None:
                endPoint = self._destinationPoint

            dx, dy = startPoint.x() - endPoint.x(), startPoint.y() - endPoint.y()

            leng = math.sqrt(dx ** 2 + dy ** 2)
            normX, normY = dx / leng, dy / leng  # normalize

            # perpendicular vector
            perpX = -normY
            perpY = normX

            leftX = endPoint.x() + self._arrow_height * normX + self._arrow_width * perpX
            leftY = endPoint.y() + self._arrow_height * normY + self._arrow_width * perpY

            rightX = endPoint.x() + self._arrow_height * normX - self._arrow_height * perpX
            rightY = endPoint.y() + self._arrow_height * normY - self._arrow_width * perpY

            point2 = QPointF(leftX, leftY)
            point3 = QPointF(rightX, rightY)

            return QPolygonF([point2, endPoint, point3])

        except (ZeroDivisionError, Exception):
            return None

    def paint(self, painter: QPainter, option, widget=None) -> None:

        painter.setRenderHint(painter.Antialiasing)

        painter.pen().setWidth(2)
        painter.setBrush(Qt.NoBrush)

        path = self.directPath()
        painter.drawPath(path)
        self.setPath(path)

        triangle_source = self.arrowCalc(path.pointAtPercent(0.1), self._sourcePoint)  # change path.PointAtPercent() value to move arrow on the line

        if triangle_source is not None:
            painter.drawPolyline(triangle_source)    

 # APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
class _MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        settings = Settings()
        self.settings = settings.items
        self.initUI()
        

    def initUI(self):
        self.widget = GoalPage()
        self.widget.show()



if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())      
                         