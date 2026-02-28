const API_KEY = "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";

async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    addMessage("Responding...", "bot");

    try {
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + API_KEY
            },
            body: JSON.stringify({
                model: "gpt-4o-mini",
                messages: [
                    { role: "system", content: "You are a helpful assistant." },
                    { role: "user", content: message }
                ]
            })
        });

        const data = await response.json();

        removeLastMessage();

        if (data.error) {
            addMessage("Error: " + data.error.message, "bot");
            console.log(data);
            return;
        }

        addMessage(data.choices[0].message.content, "bot");

    } catch (error) {
        removeLastMessage();
        addMessage("Fault somewhere :(", "bot");
        console.error(error);
    }
}

function addMessage(text, sender) {
    const chatBox = document.getElementById("chatBox");
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeLastMessage() {
    const chatBox = document.getElementById("chatBox");
    chatBox.removeChild(chatBox.lastChild);
}

document.getElementById("userInput").addEventListener("keypress", function(e) {
        if (e.key === "Enter"){ 
            sendMessage();
        }
    });