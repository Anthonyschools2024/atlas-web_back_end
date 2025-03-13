import { uploadPhoto, createUser } from "./utils.js";

/**
 * Handles the profile signup process by resolving multiple promises concurrently.
 *
 * This function uses Promise.all to collectively resolve the promises returned by
 * uploadPhoto and createUser. When both promises resolve successfully, it logs the
 * photo's body along with the user's first name and last name to the console.
 *
 * In case any of the promises reject, it logs "Signup system offline" to the console.
 *
 * @returns {Promise} A promise that resolves with an array containing the results
 *                    of uploadPhoto and createUser, or undefined if an error occurs.
 */
export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      // Destructure the results array for clarity
      const [photo, user] = results;
      // Log the expected output: photo.body, user.firstName, user.lastName
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
      return results;
    })
    .catch(() => {
      // In the event of any error in the promise chain, log the error message
      console.log("Signup system offline");
    });
}
