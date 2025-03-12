/**
 * Returns an array of student IDs from a list of student objects.
 * If the input is not an array, it returns an empty array.
 *
 * @param {Array} students - An array of student objects.
 * @returns {Array} An array of student IDs or an empty array if input is invalid.
 */
function getListStudentIds(students) {
  return Array.isArray(students) ? students.map(student => student.id) : [];
}

export default getListStudentIds;
