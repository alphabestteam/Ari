// Question 1:
const spongeBob = new Map ([
["Main character", "spongebob"],
["Best friend", "patrick"],
["pet", "gary"],
["word buddy", "squidward"],
["manager", "Mr. Krabs"],
["teacher", "Mrs. Puff"],
["location", "bikini bottom"]
]);

console.log(spongeBob)

// Question 2:
const mapKeys = Array.from(spongeBob.keys());
console.log(mapKeys);

// Question 3:
console.log(spongeBob.get("location"))

// Question 4:
console.log(spongeBob.size)

// Question 5:
console.log(spongeBob.delete("location"))

// Question 6:
console.log(spongeBob.size)

// Question 7:
console.log(spongeBob)

// Question 8:
console.log(spongeBob.has("location"))

