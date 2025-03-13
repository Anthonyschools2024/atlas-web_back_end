/**
 * Returns a rejected promise with an error message stating that the provided
 * file cannot be processed.
 *
 * @param {string} filename - The name of the file to be processed.
 * @returns {Promise<never>} A promise that immediately rejects with an Error.
 */
export default function uploadPhoto(filename) {
  return Promise.reject(new Error(`${filename} cannot be processed`));
}
