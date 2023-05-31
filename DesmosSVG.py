read = "test.svg"
animate = False

# from https://github.com/mathandy/svgpathtools
from svgpathtools import svg2paths
paths, attributes = svg2paths(read)
# from https://github.com/asweigart/pyperclip
import pyperclip

# read through svg file and write desmos functions
print("\nReading from " + read)
output = ""
output += "B_{x}\left(x_{0},x_{1},x_{2},x_{3},t\\right)=x_{0}\left(-t^{3}+3t^{2}-3t+1\\right)+x_{1}\left(3t^{3}-6t^{2}+3t\\right)+x_{2}\left(-3t^{3}+3t^{2}\\right)+x_{3}\left(t^{3}\\right)\n"
output += "B_{y}\left(y_{0},y_{1},y_{2},y_{3},t\\right)=y_{0}\left(-t^{3}+3t^{2}-3t+1\\right)+y_{1}\left(3t^{3}-6t^{2}+3t\\right)+y_{2}\left(-3t^{3}+3t^{2}\\right)+y_{3}\left(t^{3}\\right)"
if animate:
    output += "\nb=0"
    
curves = 0
for path in paths:
    for curve in path:
        output += "\n"
        xstring = "B_{x}("
        ystring = "B_{y}("
        for point in curve:
            xstring += str(round(point.real, 2)) + ","
            ystring += str(round(point.imag * -1, 2)) + ","
        xstring += "t)"
        ystring += "t)"

        output += "(" + xstring + "," + ystring + ")"
        if animate:
            output += "\{0<t<b\}"
        curves += 1

# copy output to clipboard
print("Successfully read " + str(curves) + " curves")
pyperclip.copy(output)
print("Desmos input copied to clipboard!\n")