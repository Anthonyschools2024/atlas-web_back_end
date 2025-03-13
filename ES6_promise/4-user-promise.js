/**
 * Returns a resolved promise with an object containing the provided firstName and lastName.
 *
 * @param {string} firstName - The user's first name.
 * @param {string} lastName - The user's last name.
 * @returns {Promise<Object>} A promise that resolves with an object { firstName, lastName }.
 */
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
