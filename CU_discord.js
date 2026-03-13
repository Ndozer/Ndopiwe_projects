const menu_btn = document.getElementById("menu_btn");

const general_btn = document.getElementById("general");
const ann_btn = document.getElementById("announcement");
const heading = document.getElementById("display-text");

const menu_container = document.querySelector(".menu-container");
const create_btn = document.getElementById("create");
const add_btn = document.getElementById("add_btn");
const create_box = document.querySelector(".create-box");
const btn_area = document.querySelector(".btn-area");
const btn_input = document.getElementById("input-create");
add_btn.addEventListener("click", function() {

    const newCategory = document.createElement("button");
    newCategory.textContent = "##" + btn_input.value;
    newCategory.addEventListener("click", function(){
        heading.textContent = newCategory.textContent.replace("##", "");
    });
    btn_area.appendChild(newCategory);
    btn_input.value = "";
})
menu_btn.addEventListener("click", function () {
    if (menu_container.style.display == "none" || menu_container.style.display == ""){
        menu_container.style.display = "block";
    }else{
        menu_container.style.display = "none";
    }
})

create_btn.addEventListener("click", function () {
    if (create_box.style.display == "none" || create_box.style.display == ""){
        create_box.style.display = "flex";
    }else{
        create_box.style.display = "none";
    }
})
general_btn.addEventListener("click", function() {
    heading.textContent = "General"
})
ann_btn.addEventListener("click", function() {
    heading.textContent = "Announcements"
})

async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    addMessage("Responding...", "receiver");
    try{
        const data = await response.json();

        removeLastMessage();

        if (data.error) {
            addMessage("Error: " + data.error, "receiver");
            return;
        }

        addMessage(data[0].generated_text, "receiver");

    } catch (err) {
        removeLastMessage();
        addMessage("Failed to send....", "receiver");
        console.error(err);
    }
}

function addMessage(txt, usr) {
    const box = document.getElementById("discBox");
    const div = document.createElement("div");
    div.className = "message " + usr;
    div.innerText = txt;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}

function removeLastMessage() {
    const box = document.getElementById("discBox");
    box.removeChild(box.lastChild);
}

document.getElementById("userInput").addEventListener("keypress", function(e) {
        if (e.key === "Enter"){ 
            sendMessage();
        }
    });