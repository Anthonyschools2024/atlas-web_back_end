/**
 * Creates a report object from an employees list.
 * @param {object} employeesList - The employees list object.
 * @returns {object} - The report object.
 */
export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };
}
