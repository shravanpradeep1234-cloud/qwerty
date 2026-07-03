<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best Friends Challenge</title>

<style>
body{
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg,#6a11cb,#2575fc);
    color:white;
    text-align:center;
    padding:30px;
}

.container{
    max-width:700px;
    margin:auto;
    background:rgba(255,255,255,0.15);
    padding:25px;
    border-radius:15px;
    backdrop-filter: blur(8px);
}

button{
    background:#ff4081;
    color:white;
    border:none;
    padding:12px 20px;
    border-radius:8px;
    cursor:pointer;
    font-size:18px;
    margin-top:20px;
}

button:hover{
    background:#ff1f68;
}

#score{
    font-size:22px;
    margin-top:20px;
}

input{
    padding:10px;
    width:80%;
    border:none;
    border-radius:8px;
    font-size:16px;
}
</style>
</head>
<body>

<div class="container">
<h1>💖 Best Friends Challenge 💖</h1>

<h2 id="question">Press Start!</h2>

<input type="text" id="answer" placeholder="Type your answer...">

<br>

<button onclick="nextQuestion()">Next Question</button>

<div id="score">
Questions Answered: <span id="count">0</span>
</div>

</div>

<script>

const questions = [
"What's your favorite memory with me?",
"Describe me in one word.",
"What's something you've never told me?",
"If we could travel anywhere together, where would we go?",
"What's my funniest habit?",
"Who apologizes first after a fight?",
"What's your favorite photo of us?",
"What song reminds you of me?",
"What's one thing you appreciate about our friendship?",
"Would you survive a zombie apocalypse with me?"
];

let used = [];
let count = 0;

function nextQuestion(){

    if(used.length===questions.length){
        document.getElementById("question").innerHTML="🎉 Game Over! Thanks for playing!";
        return;
    }

    let index;

    do{
        index=Math.floor(Math.random()*questions.length);
    }while(used.includes(index));

    used.push(index);

    document.getElementById("question").innerHTML=questions[index];

    document.getElementById("answer").value="";

    count++;

    document.getElementById("count").innerHTML=count;
}

</script>

</body>
</html>