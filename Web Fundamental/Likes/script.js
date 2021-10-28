var likes = 0;
var likesElement = document.querySelector("#likes");

function like() {
    likes ++;
    likesElement.innerText = "likes: " + likes;
    console.log(likes)
}

var dislikes = 0;
var dislikesElement = document.querySelector("#dislikes");

function dislike() {
    dislikes++;
    dislikesElement.innerText = "dislikes: " + dislikes;
    console.log(dislikes)
}

function clear_likes() {
    likes = 0;
    dislikes= 0;
    likesElement.innerText = "likes: " + likes;
    dislikesElement.innerText = "dislikes: " + dislikes;
}

function goto() {
    onclick = document.getElementById('goto').element.innerHTML
}

var api_key = "a5e803b483ed0a85df4b57256b0e691e" 
