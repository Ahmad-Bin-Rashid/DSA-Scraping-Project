from PyQt5 import QtCore, QtWidgets


def capture_widget_geometries(parent_widget):
    return {
        widget: widget.geometry()
        for widget in parent_widget.findChildren(
            QtWidgets.QWidget,
            options=QtCore.Qt.FindDirectChildrenOnly,
        )
    }


def scale_widget_geometries(widget_geometries, base_size, current_size):
    base_width = max(base_size.width(), 1)
    base_height = max(base_size.height(), 1)
    scale_x = current_size.width() / base_width
    scale_y = current_size.height() / base_height

    for widget, geometry in widget_geometries.items():
        widget.setGeometry(
            QtCore.QRect(
                int(round(geometry.x() * scale_x)),
                int(round(geometry.y() * scale_y)),
                max(20, int(round(geometry.width() * scale_x))),
                max(20, int(round(geometry.height() * scale_y))),
            )
        )
