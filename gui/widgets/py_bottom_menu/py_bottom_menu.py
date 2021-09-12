from qt_core import *
from . py_bottom_menu_button import PyBottomMenuButton
from gui.core.functions import *

# PY LEFT MENU
# ///////////////////////////////////////////////////////////////
class PyBottomMenu(QWidget):
    def __init__(
        self,
        parent,
        dark_one = "#1b1e23",
        dark_three = "#21252d",
        dark_four = "#272c36",
        bg_one = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#568af2",
        text_foreground = "#8a95aa",
        text_active = "#dce1ec",
        duration_time = 500,
        radius = 8,
        icon_path = "icon_menu.svg",
        icon_path_close = "icon_menu_close.svg",
    ):
        super().__init__()

        # PROPERTIES
        # ///////////////////////////////////////////////////////////////
        self._dark_one = dark_one
        self._dark_three = dark_three
        self._dark_four = dark_four
        self._bg_one = bg_one
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._context_color = context_color
        self._text_foreground = text_foreground
        self._text_active = text_active
        self._duration_time = duration_time
        self._radius = radius
        self._icon_path = Functions.set_svg_icon(icon_path)
        self._icon_path_close = Functions.set_svg_icon(icon_path_close)
        self._parent = parent

        # SETUP WIDGETS
        self.setup_ui()

        # SET BG COLOR
        self.bg.setStyleSheet(f"background: {dark_one}; border-radius: {radius};")

    # ADD BUTTONS TO BOTTOM MENU
    # Add btns and emit signals
    # ///////////////////////////////////////////////////////////////
    def add_menus(self, parameters):
        if parameters != None:
            for parameter in parameters:
                _btn_icon = parameter['btn_icon']
                _btn_id = parameter['btn_id']
                _is_active = parameter['is_active']

                self.menu = PyBottomMenuButton(
                    btn_id = _btn_id,
                    dark_one = self._dark_one,
                    dark_three = self._dark_three,
                    dark_four = self._dark_four,
                    bg_one = self._bg_one,
                    icon_color = self._icon_color,
                    icon_color_hover = self._icon_color_active,
                    icon_color_pressed = self._icon_color_pressed,
                    icon_color_active = self._icon_color_active,
                    context_color = self._context_color,
                    icon_path = _btn_icon,
                    is_active = _is_active
                )

                self.central_layout.addWidget(self.menu)

    # SELECT ONLY ONE BTN
    # ///////////////////////////////////////////////////////////////
    def select_only_one(self, widget: str):
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget:
                btn.set_active(True)
            else:
                btn.set_active(False)

    # DESELECT ALL BTNs
    # ///////////////////////////////////////////////////////////////
    def deselect_all(self):
        for btn in self.findChildren(QPushButton):
            btn.set_active(False)

    # SETUP APP
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # ADD MENU LAYOUT
        self.bottom_menu_layout = QHBoxLayout(self)
        self.bottom_menu_layout.setContentsMargins(0,0,0,0)

        # ADD BG
        self.bg = QFrame()

        # Central FRAME
        self.central_frame = QFrame()

        # ADD LAYOUTS
        self._layout = QHBoxLayout(self.bg)
        self._layout.setContentsMargins(0,0,0,0)

        # CENTRAL LAYOUT
        self.central_layout = QHBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(-10,0,-10,0)
        self.central_layout.setSpacing(50)

        # ADD TOP AND BOTTOM FRAME
        self._layout.addWidget(self.central_frame, 0, Qt.AlignCenter)

        # ADD BG TO LAYOUT
        self.bottom_menu_layout.addWidget(self.bg)

        

        

