/**
 * setFromArray - creates a Set from an array, filtering out duplicate values.
 *
 * @param {Array} arr - The input array containing any type of elements.
 *
 * @returns {Set} - A Set object with unique elements from the array.
 */
export default function setFromArray(arr) {
  return new Set(arr);
}
