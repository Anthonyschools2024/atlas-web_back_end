/**
 * cleanSet - returns a string of all the set values that start with a specific string.
 * For each value that starts with startString, only the remaining part of the string is appended.
 * The resulting string consists of these parts joined by a hyphen (-).
 *
 * @param {Set} set - A set containing string values.
 * @param {String} startString - The prefix to check for in each set value.
 *
 * @returns {String} - A string with the concatenated substrings from each value that started with startString.
 *                     Returns an empty string if startString is not a string or is empty.
 */
export default function cleanSet(set, startString) {
  // If startString is not a string or is empty, return an empty string.
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  const substrings = [];
  // Iterate over each value in the set.
  for (const value of set) {
    // Check if the value is a string and starts with the provided startString.
    if (typeof value === 'string' && value.startsWith(startString)) {
      // Append the rest of the string (substring after startString).
      substrings.push(value.slice(startString.length));
    }
  }
  // Join the resulting substrings with a hyphen.
  return substrings.join('-');
}
