const request = require('request');
const { expect } = require('chai');

describe('API Integration Tests', () => {
  const API_URL = 'http://localhost:7865';

  // Test suite for the Index page
  describe('Index page', () => {
    it('should return status code 200', (done) => {
      request.get(API_URL, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });

    it('should return the correct body content', (done) => {
      request.get(API_URL, (error, response, body) => {
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });

  // New test suite for the Cart page
  describe('Cart page', () => {
    it('should return status 200 when :id is a number', (done) => {
      request.get(`${API_URL}/cart/12`, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 12');
        done();
      });
    });

    it('should return status 404 when :id is NOT a number', (done) => {
      request.get(`${API_URL}/cart/hello`, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
  });
});
