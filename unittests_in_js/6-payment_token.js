
/**
 * Returns a resolved promise with a success message if the input is true.
 * @param {boolean} success - Determines if the promise should resolve.
 * @returns {Promise|undefined} A promise that resolves with data, or undefined.
 */
const getPaymentTokenFromAPI = (success) => {
  if (success) {
    return new Promise((resolve, reject) => {
      // CORRECTED: Added the missing space between "the" and "API".
      resolve({ data: 'Successful response from the API' });
    });
  }
  // If success is false, the function implicitly returns undefined.
};

module.exports = getPaymentTokenFromAPI;
