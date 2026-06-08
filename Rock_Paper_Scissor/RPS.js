var rock = document.getElementById("rock");
var paper = document.getElementById("paper");
var scissors = document.getElementById("scissor");
const response = document.getElementById("response");
const result = document.getElementById("result");

response.style.fontSize = "5rem"; 
response.style.fontWeight = "bold";
let isCounting = false;
function update_result(userChoice){
    if (isCounting) return; 
    isCounting = true; 
    result.innerHTML = ""; 
    let count = 5; 
    response.textContent = count;
    const countdown = setInterval(() => {
        count--; 
        if (count > 0) {
            response.textContent = count;
        } else {
            clearInterval(countdown);
            const answers = [
                ["rock.png", "rock"],
                ["paper.png", "paper"],
                ["scissors.png", "scissors"]
            ];
            const random_row = Math.floor(Math.random() * answers.length);
            const res = answers[random_row][1];
            response.innerHTML = `
                <h5>Ndopiwe Bot's response: ${res}</h5>
                <img src="${answers[random_row][0]}" alt="Revealed Target" style="max-width: 200px; display: block; margin: 0 auto;">
            `;
            let winner = "";
            if (userChoice === res) {
                winner = "Draw";
            } else if (
                (userChoice === "rock" && res === "scissors") ||
                (userChoice === "paper" && res === "rock") ||
                (userChoice === "scissors" && res === "paper")
            ) {
                winner = "You";
            } else {
                winner = "Ndopiwe Bot";
            }
            result.innerHTML = `<h3>Winner: ${winner}</h3>`;
            isCounting = false; 
        }
    }, 1000);
}
rock.addEventListener("click", () => {   
    update_result("rock");
});
paper.addEventListener("click", () => {   
    update_result("paper");
});
scissors.addEventListener("click", () => {   
    update_result("scissors");
});