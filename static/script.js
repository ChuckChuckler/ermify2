let answerTxt = "";
let i = 0;

function answer(){
    let q = document.getElementById("q");
    let qVal = q.value;
    let disp = document.getElementById("display");
    if(qVal == "" || qVal == " "){
        disp.innerText = "Ask a question first!";
    }else{
        fetch("/answer", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"data":qVal})
        })

        .then(response => {
            if(!response.ok){
                console.log("response is not okay :(");
            }else{
                return response.json();
            }
        })

        .then(data=>{
            if(data.message == "euge"){
                answerTxt = data.answer;
                i = 0;
                type();
            }else{
                console.log("eheu!");
            }
        })

        .catch(error=>{
            disp.innerText = error;
        })
    }
}

function yeowch(){
    let exclams = ["Yeowch!", "D'oh!", "Oof!", "Yeowie!", "Yikes!"];
    document.getElementById("yeowch").innerText = exclams[Math.floor(Math.random() * exclams.length)];
}


function type(){
    let disp = document.getElementById("display");
    if(i < answerTxt.length){
        disp.innerText = answerTxt.substring(0, i);
        i++;
        setTimeout(type, 25);
    }
}