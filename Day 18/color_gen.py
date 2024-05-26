import colorgram

colors = colorgram.extract("painting.jpeg", 30)

rgb_list = []

for color in colors:
    rgb_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_list)

