const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with SUM, 100, 20 and log the correct total', () => {
    // Create a stub for Utils.calculateNumber that always returns 10
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Create a spy to observe console.log
    const consoleLogSpy = sinon.spy(console, 'log');

    // Call the function we are testing
    sendPaymentRequestToApi(100, 20);

    // --- Assertions ---

    // Verify that the stub was called with the correct arguments
    expect(calculateNumberStub.calledOnceWith('SUM', 100, 20)).to.be.true;

    // Verify that the console.log spy was called with the correct message
    expect(consoleLogSpy.calledOnceWith('The total is: 10')).to.be.true;

    // --- Cleanup ---

    // Restore the original methods
    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });
});
