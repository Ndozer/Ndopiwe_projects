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

const layout = document.querySelector(".layout");
const friend_container = document.querySelector(".friend-container");
const friend_input = document.getElementById("input-friend");
const add_friend_btn = document.getElementById("add_friend_btn");
const friend_btn = document.getElementById("friend_btn");
const dash = document.querySelector(".dash");

friend_btn.addEventListener("click", function () {
    if (friend_container.style.display == "none" || friend_container.style.display == ""){
        friend_container.style.display = "block";
        menu_btn.style.display = "none";
        dash.style.display = "none";
    }else{
        friend_container.style.display = "none";
        menu_btn.style.display = "block";
        dash.style.display = "block";
    }
})
add_friend_btn.addEventListener("click", function() {
    const newFriend = document.createElement("button");
    newFriend.textContent = friend_input.value;
    newFriend.style.width = "100px";
    newFriend.style.height = "80px";
    newFriend.addEventListener("click", function(){
        heading.textContent = "Chat with " + newFriend.textContent;
        loadMessages();
    });
    layout.appendChild(newFriend);
    friend_input.value = "";
})
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
        friend_btn.style.display = "none";
        dash.style.display = "none";
    }else{
        menu_container.style.display = "none";
        friend_btn.style.display = "block";
        dash.style.display = "block";
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
function loadMessages() {

    const sender = "Me";
    const receiver = heading.textContent.replace("Chat with ", "");

    if (!receiver) return;

    fetch(`Load.php?sender=${encodeURIComponent(sender)}&receiver=${encodeURIComponent(receiver)}`)
    .then(response => response.text())
    .then(data => {
        document.getElementById("discBox").innerHTML = data;
    });
}
async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    const sender = "Me"; 
    const receiver = heading.textContent.replace("Chat with ", "");
    if (!receiver || receiver === "I CU there") {
        alert("Select a friend first");
        return;
}

    try {
        await fetch("Send.php", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `sender=${sender}&receiver=${receiver}&message=${message}`
        });

        input.value = "";
        loadMessages();

    } catch (err) {
        console.error(err);
    }
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
setInterval(loadMessages, 1000);