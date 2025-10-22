//  arrays.js
const steps = ["one", "two", "three"];
function listTemplate(step) {
  return `<li>${step}</li>`; 
}
const stepsHtml = steps.map(listTemplate); // use map to convert the list from strings to HTML
document.querySelector("#myList").innerHTML = stepsHtml.join(''); // set the innerHTML

const letterGrades = ['A', 'B', 'A'];
function gradePoint(letterGrade) {
    if (letterGrade === 'A') return 4;
    if (letterGrade === 'B') return 3;
    if (letterGrade === 'C') return 2;
    if (letterGrade === 'D') return 1;
    return 0;
}
const gradePoints = letterGrades.map(gradePoint);
const gradePointsAvg = gradePoints.reduce((total, points) => total + points) / gradePoints.length;

const fruits = ['watermelon', 'peach', 'apple', 'tomato', 'grape'];
const filteredFruits = fruits.filter((fruit) => fruit.length < 6);

const numbers = [12, 34, 21, 54];
const luckyNumber = 21;
const indexOfLucky = numbers.indexOf(luckyNumber);

// let new_array = arr.map(function callback( currentValue[, index[, array]]) {
//     // return element for new_array
// }[, thisArg])