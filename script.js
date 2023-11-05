function addEvent() {

    const button = document.querySelector("button");
    const theCounter = document.getElementById("counter-display");

    let counter = 0;
    button.addEventListener("click", () => {
        theCounter.textContent = counter++;
    });
}
addEvent();