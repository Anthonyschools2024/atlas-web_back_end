/**
 * Creates an object representing employees within a department.
 * @param {string} departmentName - The name of the department.
 * @param {string[]} employees - An array of employee names.
 * @returns {object} - An object with the department name as the key and an array of employees as the value.
 */
export default function createEmployeesObject(departmentName, employees) {
  const employeesObject = {};
  employeesObject[departmentName] = employees;
  return employeesObject;
}
