const aCourse = {
  code: "CSE121b",
  name: "Javascript Language",
  sections: [
    {
        sectionNum: 1, 
        roomNum: 'STC 353', 
        enrolled: 26, 
        days: 'TTh', 
        instructor: 'Bro T'
    }, 
    {
        sectionNum: 2, 
        roomNum: 'STC 347', 
        enrolled: 28, 
        days: 'TTh', 
        instructor: 'Sis A'
    }
  ],
  changeEnrollment: function (sectionNum, add = true) {
    const sectionIndex = this.sections.findIndex(
        (section) => section.sectionNum === sectionNum
    );
    if (sectionIndex >= 0) {
        if (add) {
            this.sections[sectionIndex].enrolled++;
        }
        else {
            this.sections[sectionIndex].enrolled--;
        }
        outputSections(this.sections);
    }
  }
};

function setCourseInfo(course) {
    const courseName = document.querySelector('#course-name');
    const courseCode = document.querySelector('#course-code');
    courseName.textContent = course.name;
    courseCode.textContent = course.code;
}

function outputSections(sections) {
    const html = sections.map(sectionTemplate).join('');
    document.querySelector('#sections').innerHTML = html.join('');
}

function sectionTemplate(section) {
  return `<tr>
    <td>${section.sectionNum}</td>
    <td>${section.roomNum}</td>
    <td>${section.enrolled}</td>
    <td>${section.days}</td>
    <td>${section.instructor}</td></tr>`
}

document.querySelector("#enrollStudent").addEventListener("click", function () {
  const sectionNum = document.querySelector("#sectionNumber").value;
  aCourse.enrollStudent(sectionNum);
});
document.querySelector("#dropStudent").addEventListener("click", function () {
  const sectionNum = document.querySelector("#sectionNumber").value;
  aCourse.dropStudent(sectionNum);
});

setCourseInfo(aCourse);
outputSections(aCourse.sections);