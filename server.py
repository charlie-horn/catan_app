from flask import Flask, render_template, jsonify, request
from flask_mime import Mime
from game import Game

app = Flask(__name__)
mimetype = Mime(app)

@mimetype("text/html")
@app.route("/")
def root():
    return render_template('index.html')

@mimetype("application/javascript")
@app.route("/jquery.min.js")
def jqueryJS():
    return render_template('jquery.min.js', )

@mimetype("application/javascript")
@app.route("/catan.js")
def catanJS():
    return render_template('catan.js', )

@mimetype("text/css")
@app.route("/style.css")
def style():
    return render_template('style.css')

@app.route("/analyzeBoard", methods=['POST'])
def analyzeBoard():
    global game
    return game.analyzeBoard()

@app.route("/initGame", methods=['POST'])
def initGame():
    global game
    numPlayers = request.args['numPlayers']
    game = Game(int(numPlayers))
    return 'OK'

@app.route("/addTileInfo", methods=['POST'])
def addTileInfo():
    global game
    id = int(request.args['id'])
    val = int(request.args['val'])
    res = int(request.args['res'])
    game.board.addTileInfo(id, val, res)
    return 'Tile Added'

@app.route("/addRoad", methods=['POST'])
def addRoad():
    global game
    playerId = int(request.args['pId'])
    roadId = int(request.args['rId'])
    game.addSettlement(playerId, roadId)
    return 'OK'
@app.route("/addSettlement", methods=['POST'])
def addSettlement():
    global game
    playerId = int(request.args['pId'])
    vertexId = int(request.args['vId'])
    game.addSettlement(playerId, vertexId)
    return 'OK'
@app.route("/addCity")
def addCity():
    return 'OK'
@app.route("/placeRobber")
def placeRobber():
    return 'OK'
