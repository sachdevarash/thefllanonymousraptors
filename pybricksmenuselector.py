# Reference from 
# https://pybricks.com/project/spike-hub-menu/
from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("N", "A", "R", "S", "C")

# Based on the selection, run a program.
if selected == "N":
    # Nolan Mission
    import Map_reveal_surface_brushing
    # call mission one
elif selected == "A":
    # Ahaan's Mission
    import Main_Maission_Version_Red_To_Blue_Zone
elif selected == "R":
    # Rohin's Mission
    import FLL9_DIRECT_FORGE_WHOLIVEDTHERE
elif selected == "S":
    # Rohin's Silo Mission
    import FLL_Good_SILO
elif selected == "C":
    # Casey Mission
    import casey
