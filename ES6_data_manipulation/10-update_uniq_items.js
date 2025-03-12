/**
 * updateUniqueItems - updates all map entries with a quantity of 1 to a quantity of 100.
 *
 * @param {Map} map - A map where each key is an item and each value is its quantity.
 *
 * @throws {Error} - Throws an error with the message "Cannot process" if the provided argument is not a Map.
 *
 * @returns {void} - The map is updated in place.
 */
export default function updateUniqueItems(map) {
  // Check if the provided argument is a Map.
  if (!(map instanceof Map)) {
    throw new Error("Cannot process");
  }

  // Iterate over each key-value pair in the map.
  for (const [key, value] of map) {
    // If the quantity is 1, update it to 100.
    if (value === 1) {
      map.set(key, 100);
    }
  }
}
