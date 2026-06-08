//background
let background;
let new_width = 800;
let new_height = 600;
let context;
//Obstacles
let obstacles = [];
let obs_width = 64; //(1/8)
let obs_height = 512;
let obsX = new_width;
let obsY = 0;

let topObs;
let bottomObs;
//Physics
let velocityX = -2;//obs moving left
let velocityY = 0;//spidey jumping
let gravity = 0.4;
//Over
let gameDone = false;
//score
let score = 0;
//spiderman
let spiderwidth = 80;
let spiderheight = 80;
let spiderX = new_width/8;
let spiderY = new_height/2;
let spiderman_img;
let spiderman = {
    x: spiderX,
    y: spiderY,
    width: spiderwidth,
    height: spiderheight
}
window.onload = function() {
    background = document.getElementById("board");
    background.width = new_width;
    background.height = new_height;
    spiderCharacter = background.getContext("2d");
    //add spiderman
    //spiderCharacter.fillStyle = "blue";
    //spiderCharacter.fillRect(spiderman.x,spiderman.y,spiderman.width,spiderman.height);
    spiderman_img = new Image();
    spiderman_img.src = "spiderman2.png";
    spiderman_img.onload = function() {
        spiderCharacter.drawImage(spiderman_img,spiderman.x,spiderman.y,spiderman.width,spiderman.height);    
    }
    topObs = new Image();
    topObs.src = "./bottom_obstacle.png";  
    bottomObs = new Image();
    bottomObs.src = "./bottom_obstacle.png";  
    requestAnimationFrame(update);
    setInterval(placeObs,1500);
    document.addEventListener("keydown",spiderMotion);
}
function update(){
    requestAnimationFrame(update);
    if (gameDone){
        return;
    }
    spiderCharacter.clearRect(0,0,background.width,background.height);
    //spiderman
    velocityY += gravity;
    spiderman.y = Math.max(spiderman.y + velocityY,0);//adds limits to canvas
    spiderCharacter.drawImage(spiderman_img,spiderman.x,spiderman.y,spiderman.width,spiderman.height);
    
    if (spiderman.y > background.height){
        gameDone = true;
    }
    //obstacles
    for (let i = 0;i<obstacles.length; i++){
        let obs = obstacles[i];
        obs.x += velocityX;
        spiderCharacter.drawImage(obs.img,obs.x,obs.y,obs.width,obs.height);
        if (!obs.passed && spiderman.x > obs.x + obs.width){
            score += 0.5;//there are two obstacles so half of 1
            obs.passed = true;
        }
        if (collision(spiderman,obs)){
            gameDone = true;
        }
    }
    //clear obstacles
    while (obstacles.length > 0 && obstacles[0].x < -obs_width){
        obstacles.shift();//removes first element
    }
    //update score
    spiderCharacter.fillStyle = "white";
    spiderCharacter.font = "45px sans-serif";
    spiderCharacter.fillText(score,5,45);
}
function placeObs(){
    if (gameDone){
        return;
    }
    let r_obsY = obsY - obs_height/4 - Math.random()*(obs_height/2);
    let gap = 202;
    //let gap = background.height/4;
    let topObstacleObj = {
        img: topObs, 
        x: obsX,
        y: r_obsY, 
        width: obs_width,
        height: obs_height,
        passed: false 
    }
    obstacles.push(topObstacleObj);
    let bottomObstacleObj = {
        img: bottomObs,
        x: obsX,
        y: r_obsY + obs_height + gap,
        width: obs_width,
        height: obs_height,
        passed: false 
    }
    obstacles.push(bottomObstacleObj);
}
function spiderMotion(e){
    if (e.code == "Space"){
        velocityY = -6;//jump
        if (gameDone){
            spiderman.y = spiderY;
            obstacles = [];
            score = 0;
            gameDone = false;
        }
    } 
    if (e.code == "ArrowUp"){
        velocityY = -6;//jump
    }
    if (e.code == "KeyX"){
        velocityY = -6;//jump
    }  
}
function collision(a,b){
    return a.x < b.x + b.width && a.x + a.width > b.x && a.y < b.y + b.height && a.y + a.height > b.y;
}