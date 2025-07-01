const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  // Test suite for the 'SUM' operation
  describe('type="SUM"', () => {
    it('should return the sum of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should handle negative numbers correctly', () => {
      assert.strictEqual(calculateNumber('SUM', -1.4, -4.5), -5);
    });

    it('should handle one integer and one float', () => {
      assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    });
  });

  // Test suite for the 'SUBTRACT' operation
  describe('type="SUBTRACT"', () => {
    it('should return the difference of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should handle negative numbers correctly', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5), 3);
    });

    it('should return a positive number when a > b', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.9, 2.1), 4);
    });
  });

  // Test suite for the 'DIVIDE' operation
  describe('type="DIVIDE"', () => {
    it('should return the result of the division of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should handle division that results in an integer', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 8.4, 1.5), 4);
    });

    it('should handle negative numbers correctly', () => {
      assert.strictEqual(calculateNumber('DIVIDE', -6.3, 2.1), -3);
    });

    // Edge case: Division by zero
    it('should return "Error" when the rounded second number is 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return "Error" when the rounded second number is 0 (from a float)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 5.8, 0.2), 'Error');
    });
  });
});
