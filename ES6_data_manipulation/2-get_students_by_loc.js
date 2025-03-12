/**
 * Returns an array of student objects located in a specific city.
 *
 * @param {Array} students - An array of student objects.
 * @param {string} city - The city to filter students by.
 * @returns {Array} An array of student objects located in the specified city.
 */
function getStudentsByLocation(students, city) {
  return students.filter(student => student.location === city);
}

export default getStudentsByLocation;
