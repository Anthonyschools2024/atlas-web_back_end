const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with the correct arguments', () => {
    // Create a spy on the Utils.calculateNumber method
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

    // Call the function we are testing
    sendPaymentRequestToApi(100, 20);

    // Assert that the spy was called exactly once
    expect(calculateNumberSpy.calledOnce).to.be.true;

    // Assert that the spy was called with the specific arguments
    expect(calculateNumberSpy.calledWith('SUM', 100, 20)).to.be.true;

    // Restore the original method to avoid side effects in other tests
    calculateNumberSpy.restore();
  });
});
