// Question 3:
const mainHeading = document.getElementById("main-heading")

// Question 4:
console.log(mainHeading.id)

// Question 5:
console.log(mainHeading.className)

// Question 6:
console.log(mainHeading.classList)

// Question 7:
console.log(mainHeading.dataset)
console.log(mainHeading.getAttribute("nonStandard"))
// Question 8:
mainHeading.classList.add("bg-lightcyan", "border")

// Question 9:
console.log(mainHeading.textContent)

// Question 10:
console.log(mainHeading.textContent.trim())

// Question 11:
mainHeading.textContent = "Hello there pearl!"

// Question 12:
const newElement = document.createElement("span")
newElement.innerHTML = "its me SpongeBob!"
mainHeading.appendChild(newElement)

// Question 13:
console.log(mainHeading)

// Question 14:
const cloned = mainHeading.cloneNode(true)
console.log(cloned)

// Question 15:
const subheading = document.createElement("h2") 
subheading.textContent = "jellyfish hunting is the best"

// Question 16:
document.body.appendChild(subheading)

// Question 17:
const text = "Lorem ipsum dolor sit amet consectetur adipiscing elit," +
" urna consequat felis vehicula class ultricies mollis dictumst," +
" aenean non a in donec nulla. Phasellus ante pellentesque erat cum risus consequat imperdiet aliquam," +
" integer placerat et turpis mi eros nec lobortis taciti, vehicula nisl litora tellus ligula porttitor metus."

// Question 18:
textToArr = text.split(" ")

// Question 19:
const color = ["red", "orange", "yellow", "greeenyellow", "lightblue", "mediumpurple"]; 

// Question 20:
const randomColor = () => {
    const rancol = Math.floor(Math.random() * color.length)
    return color[rancol]
}

// Question 21:
const randomWords = document.getElementById("random-words");

// Question 22:
textToArr.forEach(word => {
    const span = document.createElement("span");
    const style = "background-color: " + randomColor();
    span.setAttribute("style", style);
    span.textContent = word;
    span.className = "random-word";
// Question 23:
    randomWords.appendChild(span);   
});



