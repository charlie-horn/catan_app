function inputGameInfo() {
    var sNumPlayers = prompt("Enter number of players : ")
    console.log("Players : " + sNumPlayers)
    $.ajax({
        url:"/initGame?numPlayers=" + sNumPlayers,
        type:'POST',
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }
    })
}

function inputTileInfo(div, id) {
    var sDiceVal = prompt("Enter dice value: ")
    var sRes = prompt("Enter resource: \n\t1 = Wood\n\t2 = Brick\n\t3 = Sheep\n\t4 = Wheat\n\t5 = Rock\n\t6 = Desert")
    var iRes = parseInt(sRes)
    var mapping = ["Wood", "Brick", "Sheep", "Wheat", "Rock", "Desert"]
    var sResLong = mapping[iRes - 1]
    div.setAttribute("data-text", sResLong + " : " + sDiceVal)
    $.ajax({
        url:"/addTileInfo?res=" + sRes + "&id=" + id + "&val=" + sDiceVal,
        type:'POST',
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }
    })
}
function loadBoard() {
    var vals = [4,3,8,4,10,5,12,8,0,3,11,10,2,6,9,6,9,5,11];
    var resources = [3,5,4,5,1,3,1,1,6,2,2,4,4,5,1,3,3,2,4];
    var mapping = ["Wood", "Brick", "Sheep", "Wheat", "Rock", "Desert"]
    $('.tile').each(function(i,div) {
        var sRes = resources[i].toString()
        var sResLong = mapping[resources[i]-1]
        var sVal = vals[i].toString()
        div.setAttribute("data-text", sResLong + " : " + sVal);
        div.onmouseover = showStats();
        $.ajax({
            url:"/addTileInfo?res=" + sRes + "&id=" + i.toString() + "&val=" + sVal,
            type:'POST',
            success: function(response){
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
    })
}

function showStats(tile) {
    box = document.getElementById("statBox")
}

function submitBoard(){
    console.log("Analyzing Board...")
    $.ajax({
        url:"/analyzeBoard",
        type:'POST',
        success: function(response){
            console.log(response);
            var greenVal = 255
            var redVal = 0
            for (var vertex in response.sortedVals) {
                vertex = response.sortedVals[vertex]
                var vert = document.getElementById('v' + vertex)
                style = vert.getAttribute("style")
                greenVal = greenVal - 4.722
                redVal = 255 - greenVal
                var colour = "rgb(" + redVal + "," + greenVal + ",0);" 
                vert.setAttribute("style", style + "background: " + colour)
            }
        },
        error: function(error){
            console.log(error);
        }
        
    })
}
function showVals(vertexVals) {
    $('.settlement').each(function(i, div) {
        div.setAttribute("data-val", vertexVals(i))
    });
}
function inputRoadInfo(road, id) {
    var sPlayer = prompt("Enter player ID : ")
    var iPlayer = parseInt(sPlayer)
    var style = road.getAttribute("style")
    if (iPlayer == 1) {
        road.setAttribute("style", style + "background: #00f;")
    } else if (iPlayer == 2){
        road.setAttribute("style", style + "background: #f00;")
    } else if (iPlayer == 3) {
        road.setAttribute("style", style + "background: #0f0;")
    } else if (iPlayer == 4) {
        road.setAttribute("style", style + "background: #fff;")
    }
    $.ajax({
        url:"/addRoad?pId=" + sPlayer + "&rId=" + id.toString(),
        type:'POST',
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }  
    })
}
function inputSettlementInfo(vertex, id) {
    var sPlayer = prompt("Enter player ID : ")
    var iPlayer = parseInt(sPlayer)
    var style = vertex.getAttribute("style")
    if (iPlayer == 1) {
        vertex.setAttribute("style", style + "background: #00f;")
    } else if (iPlayer == 2){
        vertex.setAttribute("style", style + "background: #f00;")
    } else if (iPlayer == 3) {
        vertex.setAttribute("style", style + "background: #0f0;")
    } else if (iPlayer == 4) {
        vertex.setAttribute("style", style + "background: #fff;")
    }
    $.ajax({
        url:"/addSettlement?pId=" + sPlayer + "&vId=" + id.toString(),
        type:'POST',
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }
        
    })

}

function getResource(id) {
    var mapping = ["Wood", "Brick", "Sheep", "Wheat", "Rock", "Desert"]
    return mapping[id]
}
function addRoad() {}
function addSettlement() {}
function addCity() {}
function placeRobber() {}
function analyzeBoard(numPlayers, resources, numbers, settlements, cities, roads) {

}
const HTTP = new XMLHttpRequest();
