var playerCnt = 0
var turnCnt = 0
var categories = []

function runGame(){
    playerCnt = document.getElementById("playerCnt").value
    turnCnt = document.getElementById("turnCnt").value
    document.getElementById("step1").style.display = "none";
    var body = document.getElementsByTagName("body")
    var tbl = document.creat
}

onload = function() {
    document.getElementById("frmStep1").addEventListener("submit", e => {
        e.preventDefault()
        runGame()
    })
}


function addCategory(){
    var cat = document.getElementById("category").value
    if (cat) {
        var newItem = document.createElement("li")
        newItem.classList.add("list-group-item")
        newItem.innerText = cat
        document.getElementById("categories").appendChild(newItem)
        categories.push(cat)
    }
}

