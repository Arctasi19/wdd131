// Variables
const generateButton = document.querySelector("#submitButton")
const endOutput = document.querySelector("#output")

// Functions
function getUserInput() {
    let userEntry = document.querySelector("#grades").value;
    let newArr = userEntry.replace(/\s/g,'').toUpperCase().split(",");
    console.log("obtained string:", userEntry);
    console.log("obtained array:", newArr);
    return newArr;
}
function gradePoint(letterGrade) {
    if (letterGrade === 'A') return 4;
    if (letterGrade === 'B') return 3;
    if (letterGrade === 'C') return 2;
    if (letterGrade === 'D') return 1;
    return 0;
}
function calculateGPA() {
    const letterGrades = getUserInput();
    const gradePoints = letterGrades.map(gradePoint);
    const gpAvg = gradePoints.reduce((total, points) => total + points, 0) / gradePoints.length;
    console.log("Grade Points:", gradePoints);
    console.log("Gpa:", gpAvg);
    endOutput.innerHTML = `Your GPA is: ${gpAvg}`;
}   

// Event Listeners
generateButton.addEventListener("click", calculateGPA)