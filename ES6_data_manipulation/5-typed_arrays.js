/**
 * createInt8TypedArray - creates an ArrayBuffer and sets an Int8 value at a given position.
 *
 * @param {Number} length - The length of the ArrayBuffer to create.
 * @param {Number} position - The index at which to set the value.
 * @param {Number} value - The Int8 value to be set in the ArrayBuffer.
 *
 * @returns {DataView} - A DataView representing the ArrayBuffer with the set Int8 value.
 *
 * @throws {Error} - Throws "Position outside range" if the position is not valid.
 */
export default function createInt8TypedArray(length, position, value) {
  // Create a new ArrayBuffer with the specified length.
  const buffer = new ArrayBuffer(length);
  
  // Create a DataView for manipulating the buffer.
  const view = new DataView(buffer);

  // Validate that the given position is within the bounds of the ArrayBuffer.
  if (position < 0 || position >= length) {
    throw new Error("Position outside range");
  }

  // Set the Int8 value at the specified position.
  view.setInt8(position, value);

  // Return the DataView so that the changes can be inspected.
  return view;
}
