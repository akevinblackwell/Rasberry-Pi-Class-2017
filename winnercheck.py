def winnercheck(squares):
    xwin1 = ["X", "X", "X", "#", "#", "#", "#", "#", "#"]
    xwin2 = ["#", "#", "#", "X", "X", "X", "#", "#", "#"]
    xwin3 = ["#", "#", "#", "#", "#", "#", "X", "X", "X"]
    xwin4 = ["X", "#", "#", "X", "#", "#", "X", "#", "#"]
    xwin5 = ["#", "#", "X", "#", "#", "X", "#", "#", "X"]
    xwin6 = ["#", "X", "#", "#", "X", "#", "#", "X", "#"]
    xwin7 = ["X", "#", "#", "#", "X", "#", "#", "#", "X"]
    xwin8 = ["#", "#", "X", "#", "X", "#", "X", "#", "#"]

    owin1 = ["O", "O", "O", "#", "#", "#", "#", "#", "#"]
    owin2 = ["#", "#", "#", "O", "O", "O", "#", "#", "#"]
    owin3 = ["#", "#", "#", "#", "#", "#", "O", "O", "O"]
    owin4 = ["O", "#", "#", "O", "#", "#", "O", "#", "#"]
    owin5 = ["#", "#", "O", "#", "#", "O", "#", "#", "O"]
    owin6 = ["#", "O", "#", "#", "O", "#", "#", "O", "#"]
    owin7 = ["O", "#", "#", "#", "O", "#", "#", "#", "O"]
    owin8 = ["#", "#", "O", "#", "O", "#", "O", "#", "#"]

    winnerstatus = "."
    if squares[0:3] == xwin1[0:3]:
        winnerstatus = "X"

    elif squares[3:6] == xwin2[3:6]:
        winnerstatus = "X"

    elif squares[6:9] == xwin3[6:9]:
        winnerstatus = "X"
        
    elif (squares[0] == xwin4[0]) and (squares[3] == xwin4[3]) and (squares[3] == xwin4[3]):
        winnerstatus = "X"

    elif squares[2] == xwin5[2] and (squares[5] == xwin5[5]) and (squares[8] == xwin5[8]) :
        winnerstatus = "X"

    elif squares[1] == xwin6[1] and (squares[4] == xwin6[4]) and (squares[7] == xwin5[7]) :
        winnerstatus = "X"

    elif squares[0] == xwin7[0] and (squares[4] == xwin7[4]) and (squares[8] == xwin7[8]) :
        winnerstatus = "X"

    elif squares[2] == xwin8[2] and (squares[4] == xwin8[4]) and (squares[6] == xwin8[6]) :
        winnerstatus = "X"

    elif squares[0:3] == owin1[0:3]:
        winnerstatus = "O"

    elif squares[3:6] == owin2[3:6]:
        winnerstatus = "O"

    elif squares[6:9] == owin3[6:9]:
        winnerstatus = "O"
        
    elif (squares[0] == owin4[0]) and (squares[3] == owin4[3]) and (squares[3] == owin4[3]):
        winnerstatus = "O"

    elif squares[2] == owin5[2] and (squares[5] == owin5[5]) and (squares[8] == owin5[8]) :
        winnerstatus = "O"

    elif squares[1] == owin6[1] and (squares[4] == owin6[4]) and (squares[7] == owin5[7]) :
        winnerstatus = "O"

    elif squares[0] == owin7[0] and (squares[4] == owin7[4]) and (squares[8] == owin7[8]) :
        winnerstatus = "O"

    elif squares[2] == owin8[2] and (squares[4] == owin8[4]) and (squares[6] == owin8[6]) :
        winnerstatus = "O"

    elif not "." in squares:
        winnerstatus = "C"
    return winnerstatus

