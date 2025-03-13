/**
 * Appends three handlers to the provided promise:
 *  1. When the promise resolves, returns an object with:
 *       status: 200,
 *       body: 'success'
 *  2. When the promise rejects, returns an empty Error object.
 *  3. In every case, logs "Got a response from the API" to the console.
 *
 * @param {Promise} promise - A promise to handle.
 * @returns {Promise} A promise that resolves with the transformed value.
 */
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => new Error())
    .then((result) => {
      console.log("Got a response from the API");
      return result;
    });
}
