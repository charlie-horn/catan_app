from tile import Tile
from vertex import Vertex
import helper as h

class Board():
    def __init__(self):
        self.vertices = []
        self.tiles = []
        self.roads = []
        self.settlements = []
        self.initVertices()
        self.initTiles()
        self.initRoads()

    def initTiles(self):
        print("Initializing Tiles...")
        for id in range(19):
            tile = Tile()
            self.tiles.append(tile)
            #TODO take care of the tile-vertex association with the getNeighbours funciton
            h.addTiles(self, id, tile)
        return
    
    def initRoads(self):

    def initVertices(self):
        print("Initializing Veritices...")
        for i in range(54):
            self.vertices.append(Vertex(i))
        return 

    def addTileInfo(self, id, val, res):
        self.tiles[id].val = val
        self.tiles[id].res = res
        print("TILE ADDED:\n\tID: " + str(id) + "\n\tRes: " + str(res) + "\n\tVal: " + str(val))

    def analyze(self):
        print("Analyzing Board...")
        response = {}
        vertexScores = {}
        sortedVertices = []
        for i, vertex in enumerate(self.vertices):
            vertexScoreCard = vertex.getScoreCard()
            vertexScores[str(i)] = vertexScoreCard
        #sortedVertices = sorted(vertexScores, key=vertexScores.get["total"], reverse=True)
        response["vertexScores"] = vertexScores
        response["sortedVertices"] = sortedVertices
        return response