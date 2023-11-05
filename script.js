const button = document.getElementById("the-button");
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

const toggleBob = function(){
    if (bobGif.getAttribute("data-gif") == "hidden") {
        button.textContent = "hide Bob ;)";
        bobGif.style.display = "block";
        bobGif.setAttribute("data-gif", "shown");

    } else {
        button.textContent = "Show me Bob ;)";
        bobGif.style.display = "none";
        bobGif.setAttribute("data-gif", "hidden");
    }
};

