// Global state variables to track the active quiz session
let currentCorrectAnswer = "";
let currentTopic = "";
let hasAnswered = false; // Prevents clicking multiple answers for the same question

document.getElementById('generate').addEventListener('click', () => {
    const topic = document.getElementById('topic-input').value.trim();
    
    if (!topic) {
        alert('Please enter a topic first!');
        return;
    }
    
    currentTopic = topic; // Store the topic globally
    displayQuiz();
});

const categoryMap = {
    science: 17,
    computers: 18,
    math: 19,
    mythology: 20,
    sports: 21,
    geography: 22,
    history: 23
};

async function generateQuizFromAPI(userTopic) {
    const topic = userTopic.toLowerCase().trim();
    const categoryId = categoryMap[topic];
    if (!categoryId) {
        throw new Error(`Topic "${userTopic}" not supported yet. Try 'computers', 'history', or 'geography'.`);
    }

    const url = `https://opentdb.com/api.php?amount=1&category=${categoryId}&type=multiple`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.response_code === 0) {
            const quizItem = data.results[0];
            
            const options = [...quizItem.incorrect_answers];
            const randomPosition = Math.floor(Math.random() * (options.length + 1));
            options.splice(randomPosition, 0, quizItem.correct_answer);

            return {
                question: quizItem.question,
                choices: options,
                answer: quizItem.correct_answer,
                difficulty: quizItem.difficulty
            };
        } else {
            throw new Error("Could not retrieve quiz data from the server.");
        }
    } catch (error) {
        console.error("Fetch Error:", error);
        throw error;
    }
}

async function displayQuiz() {
    const displayDiv = document.getElementById('response'); 
    displayDiv.innerHTML = `<p style="margin-top: 20px; color: #0284c7;">Loading question...</p>`;
    hasAnswered = false; // Reset the answer lock for the new question

    try {
        const quizData = await generateQuizFromAPI(currentTopic);
        currentCorrectAnswer = quizData.answer; // Store the correct answer globally
        
        displayDiv.innerHTML = `
            <div class="question-container" style="margin-top: 30px; text-align: left; border-top: 2px dashed #e2e8f0; padding-top: 20px;">
                <span style="font-size: 0.8rem; background-color: #e0f2fe; color: #0369a1; padding: 4px 8px; border-radius: 4px; font-weight: bold; text-transform: uppercase;">
                    ${quizData.difficulty}
                </span>
                <h3 style="color: #1e293b; margin-top: 10px; font-size: 1.2rem; line-height: 1.5;">${quizData.question}</h3>
                
                <ul style="list-style: none; padding: 0; margin-top: 15px;">
                    ${quizData.choices.map(choice => `
                        <li class="quiz-choice" onclick="checkAnswer(this, '${choice.replace(/'/g, "\\'")}')">
                            ${choice}
                        </li>
                    `).join('')}
                </ul>

                <button id="next-btn" class="generate" style="margin-top: 20px; display: none; background-color: #059669;">
                    Next
                </button>
            </div>
        `;
        document.getElementById('next-btn').addEventListener('click', displayQuiz);

    } catch (err) {
        displayDiv.innerHTML = ""; 
        alert(err.message);
    }
}
function checkAnswer(selectedElement, selectedChoice) {
    if (hasAnswered) return; // Stop execution if they already guessed
    hasAnswered = true;
    const choices = document.querySelectorAll('.quiz-choice');    
    if (selectedChoice === currentCorrectAnswer) {
        selectedElement.style.borderColor = "#10b981";
        selectedElement.style.backgroundColor = "#ecfdf5";
        selectedElement.style.color = "#065f46";
    } else {
        selectedElement.style.borderColor = "#ef4444";
        selectedElement.style.backgroundColor = "#fef2f2";
        selectedElement.style.color = "#991b1b";

        // Find and highlight the correct answer in green so the user learns
        choices.forEach(choice => {
            if (choice.textContent.trim() === currentCorrectAnswer) {
                choice.style.borderColor = "#10b981";
                choice.style.backgroundColor = "#ecfdf5";
                choice.style.color = "#065f46";
            }
        });
    }
    // Disable the hover pointer interactions on all choices after validation
    choices.forEach(choice => choice.style.pointerEvents = "none");
    document.getElementById('next-btn').style.display = "block";
}