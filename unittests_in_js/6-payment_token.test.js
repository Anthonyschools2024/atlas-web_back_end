const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', () => {
  // The 'done' argument is crucial for telling Mocha when the async test is complete.
  it('should return a resolved promise with the correct data when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // Assertions are placed inside the .then() block
        expect(response).to.be.an('object');
        expect(response).to.deep.equal({ data: 'Successful response from the API' });

        // Call done() to signal that the test is complete.
        done();
      })
      .catch((err) => {
        // Fail the test if the promise is unexpectedly rejected.
        done(err);
      });
  });
});
