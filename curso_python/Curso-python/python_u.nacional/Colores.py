color = input()
list(color)

valor_r = color[1]+ color[2]

valor_g = color[3]+ color[4]

valor_b = color[5]+ color[6]


valor_r = int(f"{valor_r}", 16)
valor_g = int(f"{valor_g}", 16)
valor_b = int(f"{valor_b}", 16)

color_rgb = print (f"R: {valor_r} G: {valor_g} B: {valor_b}")


