document.addEventListener("DOMContentLoaded", function() {

let correctbox = document.getElementById("correct");
correctbox.style.visibility = "hidden";

let incorrectbox = document.getElementById("incorrect");
incorrectbox.style.visibility = "hidden";
});

async function fetchres() {
  let news = document.getElementById("news");

  const data = { input_data: [news.value] };
  
  let res = await fetch("http://localhost:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    
  let result = await res.json();
  console.log(data); // print the data
  console.log(result);

  if(result.prediction[0] == "REAL"){
    let correctbox = document.getElementById("correct");
    correctbox.style.visibility = "visible";
    let incorrectbox = document.getElementById("incorrect");
    incorrectbox.style.visibility = "hidden";
  }
  else {
    let incorrectbox = document.getElementById("incorrect");
    incorrectbox.style.visibility = "visible";
    let correctbox = document.getElementById("correct");
    correctbox.style.visibility = "hidden";
  }


}