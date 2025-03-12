/**
 * cleanSet - returns a string of all the set values that start with a specific string.
 * For each value that starts with startString, only the remaining part of the string is appended.
 * The resulting string consists of these parts joined by a hyphen (-).
 *
 * @param {Set} set - A set containing string values.
 * @param {String} startString - The prefix to check for in each set value.
 *
 * @returns {String} - A string with the concatenated substrings from each value that started with startString.
 *                     If startString is an empty string, returns an empty string.
 */
export default function cleanSet(set, startString) {
  // If startString is empty, per task expectations, return an empty string.
  if (startString === '') {
    return '';
  }

  const substrings = [];
  // Iterate over each value in the set.
  for (const value of set) {
    // Ensure the value is a string and starts with the provided startString.
    if (typeof value === 'string' && value.startsWith(startString)) {
      // Append the rest of the string (i.e., the substring after startString).
      substrings.push(value.slice(startString.length));
    }
  }
  // Join the resulting substrings with a hyphen.
  return substrings.join('-');
}
