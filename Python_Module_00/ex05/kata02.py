# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

print(str(f"{kata[1]:02d}") +
      "/" +
      str(f"{kata[2]:02d}") +
      "/" +
      str(f"{kata[0]:04d}"),
      str(f"{kata[3]:02d}") +
      ":" +
      str(f"{kata[4]:02d}")
      )
