/**
 * Returns the sum of all student IDs.
 *
 * @param {Array} students - The list of students.
 * @returns {number} The sum of student IDs.
 */
function getStudentIdsSum(students) {
  return students.reduce((sum, student) => sum + student.id, 0);
}

export default getStudentIdsSum;
