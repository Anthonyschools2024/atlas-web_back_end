// Import the Node.js built-in assertion library
const assert = require('assert');

// Import the function to be tested
const calculateNumber = require('./0-calcul.js');

// Describe the test suite for the calculateNumber function
describe('calculateNumber', () => {
  // Test case 1: Both numbers are integers
  it('should return the correct sum when both inputs are integers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  // Test case 2: One number is a float that rounds up
  it('should round the second number up and return the correct sum', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  // Test case 3: One float rounds down, one rounds up
  it('should round one number down and one up, then return the correct sum', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  // Test case 4: A number is exactly .5, which should round up
  it('should round a number ending in .5 up and return the correct sum', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // Test case 5: Both numbers are floats that round down
  it('should round both numbers down and return the correct sum', () => {
    assert.strictEqual(calculateNumber(1.4, 3.4), 4);
  });

  // Test case 6: One number is zero
  it('should handle zero correctly', () => {
    assert.strictEqual(calculateNumber(0, 5.8), 6);
  });

  // Test case 7: Both numbers are negative
  it('should work with negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
  });

  // Test case 8: One negative and one positive number
  it('should work with a mix of positive and negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.6, 3.2), -2 + 3);
  });
});
