function fetchValues() {
    let n = 1;
    let values = [];
    while (n > 0) {
        let id = "inp" + n.toString();
        console.log(id)
        let val = document.getElementById(id).value;
        values.push(val);
        n--;
    }
    return values;
}

function sendData(d) {
    axios
        .post("/eval", d)
        .then(function(response) {
            console.log(response);
        })
        .catch(function(error) {
            console.log("Please Contact Administrator " + error.toString());
        });
}

let bt = document.getElementById('butt');

bt.addEventListener("click", (e) => {
    sendData(fetchValues());
});