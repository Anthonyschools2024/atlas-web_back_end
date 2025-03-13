/**
 * Returns a Promise that immediately resolves.
 *
 * This function simulates an API call by returning a Promise that resolves immediately.
 * It adheres to the requirement "Keep every promise you make and only make promises you can keep."
 *
 * @returns {Promise} A promise that resolves with a sample API response.
 */
export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    resolve("API response");
  });
}
