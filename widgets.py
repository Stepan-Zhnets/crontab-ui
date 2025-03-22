# Widgets
def print_info(widget, depth=0):
    widget_class=widget.winfo_class()
    widget_children=widget.winfo_children()
    widget_parent=widget.winfo_parent()
    widget_toplevel=widget.winfo_toplevel()

    widget_width = widget.winfo_width()
    widget_height = widget.winfo_height()
    widget_reqwidth = widget.winfo_reqwidth()
    widget_reqheight = widget.winfo_reqheight()

    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    widget_rootx = widget.winfo_rootx()
    widget_rooty = widget.winfo_rooty()

    widget_viewable = widget.winfo_viewable()

    print("   "*depth + f"""
Class={widget_class}
Children={widget_children}
Parent={widget_parent}
Toplevel={widget_toplevel}
    width={widget_width} | height={widget_height}
    req-width={widget_reqwidth} | req-height={widget_reqheight}
    x={widget_x} | y={widget_y}
    root-x={widget_rootx} | rooty={widget_rooty}
    viewable={widget_viewable}
""")
    for child in widget.winfo_children():
        print_info(child, depth+1)