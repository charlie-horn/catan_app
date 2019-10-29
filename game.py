from player import Player
from board import Board

class Game():
    def __init__(self, numPlayers):
        self.players = self.initPlayers(numPlayers)
        self.board = Board()
        return

    def initPlayers(self, numPlayers):
        print("Initializing Players...")
        players = []
        for id in range(numPlayers):
            players.append(Player(id + 1))
        return players

    def addSettlement(self, playerId, vertexId):
        for vertex in self.board.vertices:
            if vertex.id == vertexId:
                vertex.isAvailable = False
                for neighbour in vertex.neighbours:
                    neighbour.isAvailable = False

        for player in self.players:
            if player.id == playerId:
                player.settlements.append(vertexId)
                print("Added a settlement for Player " + str(playerId))
    
    def addRoad(self, playerId, roadId):
        #TODO initialize all roads with an ID
        #TODO give each road the end and start vertices
        pass

    def analyzeBoard(self):
        print("Analyzing Game...")
        return self.board.analyze()