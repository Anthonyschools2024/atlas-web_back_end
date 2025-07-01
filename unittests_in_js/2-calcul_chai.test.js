const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  // Test suite for the 'SUM' operation using Chai
  describe('type="SUM"', () => {
    it('should return the sum of two rounded numbers', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should handle negative numbers correctly', () => {
      expect(calculateNumber('SUM', -1.4, -4.5)).to.equal(-5);
    });

    it('should handle one integer and one float', () => {
      expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    });
  });

  // Test suite for the 'SUBTRACT' operation using Chai
  describe('type="SUBTRACT"', () => {
    it('should return the difference of two rounded numbers', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should handle negative numbers correctly', () => {
      expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3);
    });

    it('should return a positive number when a > b', () => {
      expect(calculateNumber('SUBTRACT', 5.9, 2.1)).to.equal(4);
    });
  });

  // Test suite for the 'DIVIDE' operation using Chai
  describe('type="DIVIDE"', () => {
    it('should return the result of the division of two rounded numbers', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should handle division that results in an integer', () => {
      expect(calculateNumber('DIVIDE', 8.4, 1.5)).to.equal(4);
    });

    it('should handle negative numbers correctly', () => {
      expect(calculateNumber('DIVIDE', -6.3, 2.1)).to.equal(-3);
    });

    // Edge case: Division by zero
    it('should return "Error" when the rounded second number is 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return "Error" when the rounded second number is 0 (from a float)', () => {
      expect(calculateNumber('DIVIDE', 5.8, 0.2)).to.equal('Error');
    });
  });
});
