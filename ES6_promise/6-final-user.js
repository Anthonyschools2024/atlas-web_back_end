import signUpUser from "./4-user-promise.js";
import uploadPhoto from "./5-photo-reject.js";

/**
 * Handles profile signup by concurrently processing user signup and photo upload.
 *
 * This function calls signUpUser and uploadPhoto with the provided arguments.
 * It then waits for all the promises to settle using Promise.allSettled.
 *
 * Once settled, it returns an array where each element is an object with:
 *   - status: the status of the promise ("fulfilled" or "rejected")
 *   - value: the resolved value, or the error message (as a string) if the promise was rejected
 *
 * @param {string} firstName - The first name of the user.
 * @param {string} lastName - The last name of the user.
 * @param {string} fileName - The name of the file to be uploaded.
 * @returns {Promise<Array<{ status: string, value: any }>>} A promise that resolves
 *          to an array of objects describing the outcome of each promise.
 */
export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) =>
      results.map((result) => {
        if (result.status === "rejected") {
          // Convert the error object to a string to match the expected output.
          return { status: result.status, value: result.reason.toString() };
        }
        return { status: result.status, value: result.value };
      })
    );
}

