function findSeashellsIndicies(target, values) {
    for (const number of values) {
        check = target - number
        if (values.includes(check)) { 
        return [values.indexOf(number), values.indexOf(check)]
        } else {
            return []
        }
    }
};
//  for example:
let calculate = findSeashellsIndicies(30, [25, 21, 15, 10, 5])
console.log(calculate)