# Put this at the top of your kata02.py file
kata = (8, 32, 2022, 12, 1)

print(str(f"{kata[1]:02d}") +
      "/" +
      str(f"{kata[2]:02d}") +
      "/" +
      str(f"{kata[0]:04d}"),
      str(f"{kata[3]:02d}") +
      ":" +
      str(f"{kata[4]:02d}")
      )
