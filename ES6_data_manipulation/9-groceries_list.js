/**
 * groceriesList - returns a map of groceries with predefined items and their quantities.
 *
 * @returns {Map} - A Map where each key is the name of a grocery item and its value is the quantity.
 */
export default function groceriesList() {
  return new Map([
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5]
  ]);
}
