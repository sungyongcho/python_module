# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print(
    "module_" + str(f"{kata[0]:02d}") + ",",
    "ex_" + str(f"{kata[1]:02d}"), ":",
    str(f"{kata[2]:.2f}") + ",",
    str(f"{kata[3]:.2e}") + ",",
    str(f"{kata[4]:.2e}")
    )
