const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi', () => {
  let consoleLogSpy;

  // Before each test, create a fresh spy
  beforeEach(() => {
    consoleLogSpy = sinon.spy(console, 'log');
  });

  // After each test, restore the spy to its original state
  afterEach(() => {
    consoleLogSpy.restore();
  });

  it('should log "The total is: 120" when called with 100 and 20', () => {
    // Act: Call the function for the first test case
    sendPaymentRequestToApi(100, 20);

    // Assert: Verify console.log was called correctly
    expect(consoleLogSpy.calledOnceWith('The total is: 120')).to.be.true;
    expect(consoleLogSpy.calledOnce).to.be.true;
  });

  it('should log "The total is: 20" when called with 10 and 10', () => {
    // Act: Call the function for the second test case
    sendPaymentRequestToApi(10, 10);

    // Assert: Verify console.log was called correctly
    expect(consoleLogSpy.calledOnceWith('The total is: 20')).to.be.true;
    expect(consoleLogSpy.calledOnce).to.be.true;
  });
});
