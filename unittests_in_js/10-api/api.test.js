const request = require('request');
const { expect } = require('chai');

describe('API Integration Tests', () => {
  const API_URL = 'http://localhost:7865';

  describe('Index page', () => {
    it('should return status code 200', (done) => {
      request.get(API_URL, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });
  });

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

  // New test suite for the /available_payments endpoint
  describe('Available Payments page', () => {
    it('should return the correct payment methods object', (done) => {
      request.get(`${API_URL}/available_payments`, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        const expectedBody = {
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        };
        // Use deep.equal for object comparison
        expect(JSON.parse(body)).to.deep.equal(expectedBody);
        done();
      });
    });
  });

  // New test suite for the /login endpoint
  describe('Login page', () => {
    it('should welcome the user with their username', (done) => {
      const options = {
        url: `${API_URL}/login`,
        method: 'POST',
        json: true, // Automatically stringifies the body to JSON
        body: {
          userName: 'Betty'
        }
      };

      request(options, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      });
    });
  });
});
