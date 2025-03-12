/**
 * Returns an array of students for a specific city with their new grades.
 *
 * @param {Array} students - The list of students.
 * @param {string} city - The city to filter students by.
 * @param {Array} newGrades - An array of grade objects with studentId and grade.
 * @returns {Array} An array of student objects with their grades updated.
 */
function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter(student => student.location === city)
    .map(student => {
      const gradeObj = newGrades.find(grade => grade.studentId === student.id);
      return { ...student, grade: gradeObj ? gradeObj.grade : 'N/A' };
    });
}

export default updateStudentGradeByCity;
