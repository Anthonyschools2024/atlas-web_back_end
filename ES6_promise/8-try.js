/**
 * Divides the numerator by the denominator.
 *
 * If the denominator is equal to 0, an error is thrown with the message "cannot divide by 0".
 * Otherwise, the function returns the result of the division.
 *
 * @param {number} numerator - The number to be divided.
 * @param {number} denominator - The number by which to divide.
 * @returns {number} The quotient of the division.
 * @throws {Error} If the denominator is 0.
 */
export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
