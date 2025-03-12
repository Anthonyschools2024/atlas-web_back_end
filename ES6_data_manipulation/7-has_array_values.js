/**
 * hasValuesFromArray - checks if all the elements in the array exist within the set.
 *
 * @param {Set} set - The set containing elements.
 * @param {Array} arr - The array whose elements will be checked against the set.
 *
 * @returns {boolean} - Returns true if every element in the array is found in the set; otherwise, returns false.
 */
export default function hasValuesFromArray(set, arr) {
  for (const value of arr) {
    if (!set.has(value)) {
      return false;
    }
  }
  return true;
}
