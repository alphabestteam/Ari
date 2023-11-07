const quotes = [
  "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
  "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
  "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
  "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
  "The inner machinations of my mind are an enigma. - Patrick Star",
  "I can't hear you, it's too dark in here! - Patrick Star",
  "I'm ugly and I'm proud! - SpongeBob SquarePants",
  "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
  "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
  "Is mayonnaise an instrument? - Patrick Star",
  "Can you give SpongeBob his brain back? - Patrick Star",
  "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
  "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
  "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
  "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
  "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
  "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
  "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
  "SpongeBob: Can I be excused for the rest of my life?",
  "SpongeBob: I'm not just ready, I'm ready Freddy!",
  "SpongeBob: You don't need a license to drive a sandwich.",
  "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
  "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
  "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
  "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end."
];

const input = document.getElementById("input");
const button = document.getElementById("start-btn");
const text = document.getElementById("quote");
const timer = document.getElementById("timer");
let seconds = 0;
let intervalId;

function getRandomQuote() {
  const randomQuote = Math.floor(Math.random() * quotes.length);
  return quotes[randomQuote];
}

function startGame() {
  const btn = document.querySelector("button");

  btn.addEventListener("click", () => {
    result.innerHTML = "";
    input.value = "";
    input.disabled = false;
    document.getElementById("input").addEventListener("input", checkInput);
    const sentence = getRandomQuote();
    text.innerHTML = "";

    // Here I make the context that shown on the screen separated by entering each letter to span (so we can color one letter on the time). 
    for (let i = 0; i < sentence.length; i++) {
      const spans = document.createElement("span");
      spans.textContent = sentence[i];
      text.appendChild(spans);

      startTime = performance.now();
      intervalId = setInterval(function () {
        let currentTime = performance.now();
        let passTime = currentTime - startTime;
        seconds = Math.floor(passTime / 1000);
        timer.textContent = seconds;
      }, 1000);
    }
  });
}

function checkInput() {
  const spans = text.querySelectorAll("span");

  for (let i = 0; i < input.value.length; i++) {

    if (input.value[i] === spans[i].textContent) {
      spans[i].classList.add("correct");
      spans[i].classList.remove("incorrect");

    } else {
      spans[i].classList.add("incorrect");
      spans[i].classList.remove("correct");
    }
  }

  if (input.value.length === spans.length) {
    input.removeEventListener("input", checkInput);
    button.removeEventListener("click", onClickHandler);
    const inputElement = document.getElementById("input");
    inputElement.disabled = true;
    clearInterval(intervalId);
    endGame();
  }

  // if the user delete the input the colors are deleted too! 
  for (let i = input.value.length; i < spans.length; i++) {
    spans[i].classList.remove("correct", "incorrect");
  }
}

function countMatchingChars(strA) {
  const spans = strA.querySelectorAll("span")
  let wrongWords = 0;

  spans.forEach(span => {
    if (span.classList.contains("incorrect")) {
      wrongWords += 1;
    }
  });

  const correctWords = spans.length - wrongWords;
  const successRates = (correctWords / spans.length) * 100;
  return successRates.toFixed();
}

function endGame() {
  const result = document.getElementById("result");

  const typedWords = document.createElement("p");
  const seconds = document.createElement("p");
  const speedType = document.createElement("p");
  const success = document.createElement("p");

  const writtenWords = text.textContent.split(" ");
  const passTime = parseFloat(timer.textContent);
  const speed = (writtenWords.length / passTime) * 60;
  const present = countMatchingChars(text);

  typedWords.textContent = `You typed ${writtenWords.length} words!`;
  seconds.textContent = `In ${timer.textContent} seconds!`;
  speedType.textContent = `Your speed is ${speed.toFixed()} wpm!`;
  success.textContent = `With ${present}% accuracy!`;

  result.appendChild(typedWords);
  result.appendChild(seconds);
  result.appendChild(speedType);
  result.appendChild(success);
}

function onClickHandler() {
  input.disabled = false;
  input.focus();
  let startTime = performance.now();
  intervalId = setInterval(function () {
    let currentTime = performance.now();
    let passTime = currentTime - startTime;
    seconds = Math.floor(passTime / 1000);
    timer.textContent = seconds;
  }, 1000);
}

button.addEventListener("click", onClickHandler);
startGame()
document.getElementById("input").addEventListener("input", checkInput);



