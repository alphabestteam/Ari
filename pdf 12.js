// Question 1 a:
function Student(name, age, grade) {
    this.name = name,
        this.age = age,
        this.grade = grade,
        this.avg = average = () => {
            const match = name.match(/[aeiou]/gi);
            if (match) {
                return average = (grade.reduce((a, b) => a + b, 0) / grade.length) + match.length;
            }
            return average = grade.reduce((a, b) => a + b, 0) / grade.length;
        }
}

const student1 = new Student("Ari", 22, [91, 82, 93, 84])
const student2 = new Student("Daniel", 21, [100, 20, 33, 46])
const student3 = new Student("Hen", 20, [51, 52, 73, 94])
const student4 = new Student("David", 19, [71, 82, 63, 74])
const student5 = new Student("Ezra", 18, [81, 52, 93, 84])

// Question 1 b:
const students = [student1, student2, student3, student4, student5]

// Question 1 c:
for (const student of students) {
    console.log(students.indexOf(student), student)
}

// Question 1 d:
const adults = students.filter(student => student.age > 18)
console.log(adults)



// Question 2 a:
function myCar(manufacturer, model, year) {
    this.manufacturer = manufacturer,
        this.model = model,
        this.year = year,
        this.age = age = () => {
            currentDate = new Date();
            const age = currentDate.getFullYear() - this.year;
            return age
        }
}

const car1 = new myCar("Toyota", "Rav4", 2020)
const car2 = new myCar("Toyota", "CHR", 2021)
const car3 = new myCar("Toyota", "Corolla", 2022)
const car4 = new myCar("Toyota", "Camry", 2023)
const car5 = new myCar("Toyota", "Yaris", 2019)

// Question 2 b:
const cars = [car1, car2, car3, car4, car5]
for (const car of cars) {
    console.log(cars.indexOf(car), car)
}

