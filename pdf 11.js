// question 1;
function helloWorld () {
    return "Hello World";
}

// question 2;
function helloName (name) {
    return "hello " + name
}

// question 3;
const powNum = (num) => num ** 2

// question 4;
const rectangleCalculate = (length, width) => length*width

// question 5;
const circleCalculate = (radius) => {
    const pi = Math.PI
    const powRadius = Math.pow(radius,2)
    const circumference = 2 * pi * radius;
    const area = 2 * pi * powRadius;
    return [circumference, area];
}

// question 6;
const vowelsCount = (str) => {
    const match = str.match(/[aeiou]/gi);
    if (match) {
        const count = match.length 
        return count;
    } else {
        return 0;
    }
} 

// question 7;
const twoArray = (arr1, arr2) => arr1.length == arr2.length

// question 8;
const numToArr = (num) => Array.from(String(num), Number);


// question 9;
const booleanArr = (arr) => {
    return arr.map(Boolean)
}




