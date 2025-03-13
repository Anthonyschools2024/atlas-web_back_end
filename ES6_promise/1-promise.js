/**
 * Returns a promise that simulates an API response.
 *
 * If the provided parameter is true, the promise resolves with an object:
 *   { status: 200, body: 'Success' }
 *
 * If the parameter is false, the promise rejects with an error object containing the message:
 *   "The fake API is not working currently"
 *
 * @param {boolean} success - Determines whether the API call is simulated as successful.
 * @returns {Promise} A promise representing the simulated API call.
 */
export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ status: 200, body: 'Success' });
    } else {
      reject(new Error("The fake API is not working currently"));
    }
  });
}
