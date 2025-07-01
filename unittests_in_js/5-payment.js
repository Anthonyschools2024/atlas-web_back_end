const Utils = require('./utils');

/**
 * Calls the Utils.calculateNumber function and logs the result.
 * @param {number} totalAmount - The total amount.
 * @param {number} totalShipping - The shipping cost.
 */
const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${total}`);
};

module.exports = sendPaymentRequestToApi;
