import helper as h 

class Vertex():
    def __init__(self, id):
        self.id = id
        self.primaryScore = 0.
        self.secondaryScore = 0.
        self.totalScore = 0.
        self.secondaryCoefficient = 0.2
        self.isAvailable = True
        self.owner = None
        self.neighbours = h.getNeighbours(self)
        self.tiles = []
    
    def isAvailable(self):
        return self.isAvailable

    def getScoreCard(self):
        primaryScore = self.getPrimaryScore()
        secondaryScore = self.getSecondaryScore()
        totalScore = primaryScore + secondaryScore
        scoreCard = {
            "primary" : primaryScore,
            "secondary" : secondaryScore,
            "total" : totalScore
        }
        return scoreCard

    def getPrimaryScore(self):
        primaryScore = 0.
        for tile in self.tiles:
            primaryScore += h.expectedVal(tile.val) 
        self.primaryScore = primaryScore
        return primaryScore

    def getSecondaryScore(self):
        secondaryScore = 0.
        neighbourScores = 0.
        for neighbour in self.neighbours:
            print("NEIGHBOUR OF " + self.id + " IS " + neighbour.id)
            neighbourScores += neighbour.getNeighbourPrimaryScores(self.id)
        secondaryScore = self.secondaryCoefficient * neighbourScores
        return secondaryScore

    def getNeighbourPrimaryScores(originalId):
        availableScore = 0.
        for neighbour in self.neighbours:
            if neighbour.id == originalId:
                next
            if not neighbour.isAvailable:
                next
            availableScore += neighbour.getPrimaryScore()
        return availableScore