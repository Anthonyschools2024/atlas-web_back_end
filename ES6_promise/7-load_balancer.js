/**
 * Returns a promise that resolves with the value of the promise that resolves first.
 *
 * This function uses Promise.race to return the value of the promise that settles (resolves or rejects) first.
 *
 * @param {Promise} chinaDownload - A promise representing a download from China.
 * @param {Promise} USDownload - A promise representing a download from the US.
 * @returns {Promise<any>} A promise that resolves with the value of the first resolved promise.
 */
export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
