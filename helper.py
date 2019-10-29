def expectedVal(diceVal):
    if diceVal == 2 or diceVal == 12:
        val = 0.02778
    elif diceVal == 3 or diceVal == 11:
        val = 0.05556
    elif diceVal == 4 or diceVal == 10:
        val = 0.08333
    elif diceVal == 5 or diceVal == 9:
        val = 0.11111
    elif diceVal == 6 or diceVal == 8:
        val = 0.13889
    elif diceVal == 0:
        val = 0
    return val

def addTiles(board,id, tile):
    if id == 0:
        board.vertices[0].tiles.append(tile)
        board.vertices[3].tiles.append(tile)
        board.vertices[4].tiles.append(tile)
        board.vertices[7].tiles.append(tile)
        board.vertices[8].tiles.append(tile)
        board.vertices[12].tiles.append(tile)
    elif id == 1:
        board.vertices[1].tiles.append(tile)
        board.vertices[4].tiles.append(tile)
        board.vertices[5].tiles.append(tile)
        board.vertices[8].tiles.append(tile)
        board.vertices[9].tiles.append(tile)
        board.vertices[13].tiles.append(tile)
    elif id == 2:
        board.vertices[2].tiles.append(tile)
        board.vertices[5].tiles.append(tile)
        board.vertices[6].tiles.append(tile)
        board.vertices[9].tiles.append(tile)
        board.vertices[10].tiles.append(tile)
        board.vertices[14].tiles.append(tile)
    elif id == 3:
        board.vertices[7].tiles.append(tile)
        board.vertices[11].tiles.append(tile)
        board.vertices[12].tiles.append(tile)
        board.vertices[16].tiles.append(tile)
        board.vertices[17].tiles.append(tile)
        board.vertices[22].tiles.append(tile)
    elif id == 4:
        board.vertices[8].tiles.append(tile)
        board.vertices[12].tiles.append(tile)
        board.vertices[13].tiles.append(tile)
        board.vertices[17].tiles.append(tile)
        board.vertices[18].tiles.append(tile)
        board.vertices[23].tiles.append(tile)
    elif id == 5:
        board.vertices[9].tiles.append(tile)
        board.vertices[13].tiles.append(tile)
        board.vertices[14].tiles.append(tile)
        board.vertices[18].tiles.append(tile)
        board.vertices[19].tiles.append(tile)
        board.vertices[24].tiles.append(tile)
    elif id == 6:
        board.vertices[10].tiles.append(tile)
        board.vertices[14].tiles.append(tile)
        board.vertices[15].tiles.append(tile)
        board.vertices[19].tiles.append(tile)
        board.vertices[20].tiles.append(tile)
        board.vertices[25].tiles.append(tile)
    elif id == 7:
        board.vertices[16].tiles.append(tile)
        board.vertices[21].tiles.append(tile)
        board.vertices[22].tiles.append(tile)
        board.vertices[27].tiles.append(tile)
        board.vertices[28].tiles.append(tile)
        board.vertices[33].tiles.append(tile)
    elif id == 8:
        board.vertices[17].tiles.append(tile)
        board.vertices[22].tiles.append(tile)
        board.vertices[23].tiles.append(tile)
        board.vertices[28].tiles.append(tile)
        board.vertices[29].tiles.append(tile)
        board.vertices[34].tiles.append(tile)
    elif id == 9:
        board.vertices[18].tiles.append(tile)
        board.vertices[23].tiles.append(tile)
        board.vertices[24].tiles.append(tile)
        board.vertices[29].tiles.append(tile)
        board.vertices[30].tiles.append(tile)
        board.vertices[35].tiles.append(tile)
    elif id == 10:
        board.vertices[19].tiles.append(tile)
        board.vertices[24].tiles.append(tile)
        board.vertices[25].tiles.append(tile)
        board.vertices[30].tiles.append(tile)
        board.vertices[31].tiles.append(tile)
        board.vertices[36].tiles.append(tile)
    elif id == 11:
        board.vertices[20].tiles.append(tile)
        board.vertices[25].tiles.append(tile)
        board.vertices[26].tiles.append(tile)
        board.vertices[31].tiles.append(tile)
        board.vertices[32].tiles.append(tile)
        board.vertices[37].tiles.append(tile)
    elif id == 12:
        board.vertices[28].tiles.append(tile)
        board.vertices[33].tiles.append(tile)
        board.vertices[34].tiles.append(tile)
        board.vertices[38].tiles.append(tile)
        board.vertices[39].tiles.append(tile)
        board.vertices[43].tiles.append(tile)
    elif id == 13:
        board.vertices[29].tiles.append(tile)
        board.vertices[34].tiles.append(tile)
        board.vertices[35].tiles.append(tile)
        board.vertices[39].tiles.append(tile)
        board.vertices[40].tiles.append(tile)
        board.vertices[44].tiles.append(tile)
    elif id == 14:
        board.vertices[30].tiles.append(tile)
        board.vertices[35].tiles.append(tile)
        board.vertices[36].tiles.append(tile)
        board.vertices[40].tiles.append(tile)
        board.vertices[41].tiles.append(tile)
        board.vertices[45].tiles.append(tile)
    elif id == 15:
        board.vertices[31].tiles.append(tile)
        board.vertices[36].tiles.append(tile)
        board.vertices[37].tiles.append(tile)
        board.vertices[41].tiles.append(tile)
        board.vertices[42].tiles.append(tile)
        board.vertices[46].tiles.append(tile)
    elif id == 16:
        board.vertices[39].tiles.append(tile)
        board.vertices[43].tiles.append(tile)
        board.vertices[44].tiles.append(tile)
        board.vertices[47].tiles.append(tile)
        board.vertices[48].tiles.append(tile)
        board.vertices[51].tiles.append(tile)
    elif id == 17:
        board.vertices[40].tiles.append(tile)
        board.vertices[44].tiles.append(tile)
        board.vertices[45].tiles.append(tile)
        board.vertices[48].tiles.append(tile)
        board.vertices[49].tiles.append(tile)
        board.vertices[52].tiles.append(tile)
    elif id == 18:
        board.vertices[41].tiles.append(tile)
        board.vertices[45].tiles.append(tile)
        board.vertices[46].tiles.append(tile)
        board.vertices[49].tiles.append(tile)
        board.vertices[50].tiles.append(tile)
        board.vertices[53].tiles.append(tile)
    pass

def getNeighbours(vertex):
    if vertex.id == 0:
        neighbours = []
    elif vertex.id == 1:
        neighbours = []
    elif vertex.id == 2:
        neighbours = []
    elif vertex.id == 3:
        neighbours = []
    elif vertex.id == 4:
        neighbours = []
    elif vertex.id == 5:
        neighbours = []
    elif vertex.id == 6:
        neighbours = []
    elif vertex.id == 7:
        neighbours = []
    elif vertex.id == 8:
        neighbours = []
    elif vertex.id == 9:
        neighbours = []
    elif vertex.id == 10:
        neighbours = []
    elif vertex.id == 11:
        neighbours = []
    elif vertex.id == 12:
        neighbours = []
    elif vertex.id == 13:
        neighbours = []
    elif vertex.id == 14:
        neighbours = []
    elif vertex.id == 15:
        neighbours = []
    elif vertex.id == 16:
        neighbours = []
    elif vertex.id == 17:
        neighbours = []
    elif vertex.id == 18:
        neighbours = []
    elif vertex.id == 19:
        neighbours = []
    elif vertex.id == 20:
        neighbours = []
    elif vertex.id == 21:
        neighbours = []
    elif vertex.id == 22:
        neighbours = []
    elif vertex.id == 23:
        neighbours = []
    elif vertex.id == 24:
        neighbours = []
    elif vertex.id == 25:
        neighbours = []
    elif vertex.id == 26:
        neighbours = []
    elif vertex.id == 27:
        neighbours = []
    elif vertex.id == 28:
        neighbours = []
    elif vertex.id == 29:
        neighbours = []
    elif vertex.id == 30:
        neighbours = []
    elif vertex.id == 31:
        neighbours = []
    elif vertex.id == 32:
        neighbours = []
    elif vertex.id == 33:
        neighbours = []
    elif vertex.id == 34:
        neighbours = []
    elif vertex.id == 35:
        neighbours = []
    elif vertex.id == 36:
        neighbours = []
    elif vertex.id == 37:
        neighbours = []
    elif vertex.id == 38:
        neighbours = []
    elif vertex.id == 39:
        neighbours = []
    elif vertex.id == 40:
        neighbours = []
    elif vertex.id == 41:
        neighbours = []
    elif vertex.id == 42:
        neighbours = []
    elif vertex.id == 43:
        neighbours = []
    elif vertex.id == 44:
        neighbours = []
    elif vertex.id == 45:
        neighbours = []
    elif vertex.id == 46:
        neighbours = []
    elif vertex.id == 47:
        neighbours = []
    elif vertex.id == 48:
        neighbours = []
    elif vertex.id == 49:
        neighbours = []
    elif vertex.id == 50:
        neighbours = []
    elif vertex.id == 51:
        neighbours = []
    elif vertex.id == 52:
        neighbours = []
    elif vertex.id == 53:
        neighbours = []
    return neighbours

