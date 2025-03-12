import tkinter

def clean_coordinate(coords: list) -> None:
    x_min = min([coords[i][0] for i in range(len(coords))])
    y_min = min([coords[i][1] for i in range(len(coords))])
    for i in range(len(coords)):
        coords[i][0] -= x_min
        coords[i][1] -= y_min


def get_coordinates():
    output = []
    for i in range(len(checkbuttons)):
        for j in range(len(checkbuttons[i])):
            if variables[i][j].get():
                output.append([i, j])
    clean_coordinate(output)
    txt.delete('1.0', "end")
    txt.insert("1.0", str(output))

#  CONSTANTS
BOX_SIDE_LENGTH = 30

m = tkinter.Tk()
f = tkinter.Frame(m, width=500, height=500)
f.grid(row=0, column=0)

checkbuttons = []

#  Variables setup
variables = []
for i in range(BOX_SIDE_LENGTH):
    variables.append([])

#  Check button setup
for x in range(BOX_SIDE_LENGTH):
    row = []
    for y in range(BOX_SIDE_LENGTH):
        variables[x].append(tkinter.IntVar())
        c = tkinter.Checkbutton(f, variable=variables[x][y])
        row.append(c)
        c.grid(row=y, column=x)
    checkbuttons.append(row)
btn = tkinter.Button(m, text="Generate Coordinates", command=get_coordinates)
btn.grid(row=0, column=1)

txt = tkinter.Text(m, width=50)
txt.grid(row=0, column=2)

m.mainloop()
