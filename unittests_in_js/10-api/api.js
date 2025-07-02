const express = require('express');

const app = express();
const PORT = 7865;

// Middleware to parse JSON bodies. This is crucial for the /login endpoint.
app.use(express.json());

// Handler for the root endpoint GET /
app.get('/', (req, res) => {
  res.status(200).send('Welcome to the payment system');
});

// Handler for the cart endpoint with regex validation
app.get('/cart/:id(\\d+)', (req, res) => {
  const { id } = req.params;
  res.status(200).send(`Payment methods for cart ${id}`);
});

// New endpoint for available payment methods
app.get('/available_payments', (req, res) => {
  res.status(200).json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// New endpoint for user login
app.post('/login', (req, res) => {
  // Get the userName from the request body
  const { userName } = req.body;
  if (userName) {
    res.status(200).send(`Welcome ${userName}`);
  } else {
    res.status(400).send('Bad Request'); // Handle case where userName is not provided
  }
});

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;
