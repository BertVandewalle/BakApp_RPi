import os
from qt_core import *
from gui.core.functions import *

# BOTTOM MENU   
# ///////////////////////////////////////////////////////////////
class PyBottomMenuButton(QPushButton):
    def __init__(
        self,
        parent = None,
        btn_id = None,
        margin = 3,
        dark_one = "#1b1e23",
        dark_three = "#21252d",
        dark_four = "#272c36",
        bg_one = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#568af2",
        icon_path = "icon_home.svg",
        icon_active_menu = "active_menu_bot.svg",
        is_active = False,
    ):
        super().__init__()
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.setObjectName(btn_id)
        self.setMinimumWidth(90)
        self.setMaximumWidth(90)

        # APP PATH
        self._icon_path = Functions.set_svg_icon(icon_path)
        self._icon_active_menu = Functions.set_svg_icon(icon_active_menu)

        # PROPERTIES
        self._margin = margin
        self._dark_one = dark_one
        self._dark_three = dark_three
        self._dark_four = dark_four
        self._bg_one = bg_one
        self._context_color = context_color
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._set_icon_color = self._icon_color 
        self._set_bg_color = self._dark_one 
        self._is_active = is_active
        self._parent = parent


    # PAINT EVENT
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        # PAINTER
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        p.setFont(self.font())

        # RECTANGLES
        rect_inside = QRect(20, 4, self.width() -40, self.height() - 8)
        rect_icon = QRect(15, 0, self.width()-30, self.height())
        rect_blue = QRect(20, self.height()-24, self.width()-40, 20)
        rect_inside_active = QRect(20, -7, self.width()-40, self.height())

        if self._is_active:
            # DRAW BG BLUE
            p.setBrush(QColor(self._context_color))
            p.drawRoundedRect(rect_blue, 8, 8)

            # BG INSIDE
            p.setBrush(QColor(self._bg_one))
            p.drawRoundedRect(rect_inside_active, 8, 8)

            # DRAW ACTIVE
            icon_path = self._icon_active_menu
            app_path = os.path.abspath(os.getcwd())
            icon_path = os.path.normpath(os.path.join(app_path, icon_path))
            self._set_icon_color = self._icon_color_active
            self.icon_active(p, icon_path, self.width())

            # DRAW ICONS
            self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color) 
       
        # NORMAL BG
        else:
            # BG INSIDE
            p.setBrush(QColor(self._set_bg_color))
            p.drawRoundedRect(rect_inside, 8, 8)

            # DRAW ICONS
            self.icon_paint(p, self._icon_path, rect_icon, self._set_icon_color)        

        p.end()

    # SET ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        if not is_active:
            self._set_icon_color = self._icon_color
            self._set_bg_color = self._dark_one

        self.repaint()


    # RETURN IF IS ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        return self._is_active
    
    # SET ICON
    # ///////////////////////////////////////////////////////////////
    def set_icon(self, icon_path):
        self._icon_path = icon_path
        self.repaint()

    # DRAW ICON WITH COLORS
    # ///////////////////////////////////////////////////////////////
    def icon_paint(self, qp, image, rect, color):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), QColor(color))
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2+15, 
            (rect.height() - icon.height()) / 2,
            icon
        )        
        painter.end()

    # DRAW ACTIVE ICON
    # ///////////////////////////////////////////////////////////////
    def icon_active(self, qp, image, height):
        icon = QPixmap(image)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), QColor(self._bg_one))
        qp.drawPixmap(0,0, icon)
        painter.end()


    
