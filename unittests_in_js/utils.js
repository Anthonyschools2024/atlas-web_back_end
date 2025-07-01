/**
 * A utility module for calculations.
 */
const Utils = {
  /**
   * Performs SUM, SUBTRACT, or DIVIDE operations on two rounded numbers.
   * @param {string} type - The type of operation (SUM, SUBTRACT, DIVIDE).
   * @param {number} a - The first number.
   * @param {number} b - The second number.
   * @returns {number|string} The result of the operation or 'Error' for division by zero.
   */
  calculateNumber: (type, a, b) => {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    switch (type) {
      case 'SUM':
        return roundedA + roundedB;
      case 'SUBTRACT':
        return roundedA - roundedB;
      case 'DIVIDE':
        if (roundedB === 0) {
          return 'Error';
        }
        return roundedA / roundedB;
      default:
        break;
    }
  }
};

module.exports = Utils;
