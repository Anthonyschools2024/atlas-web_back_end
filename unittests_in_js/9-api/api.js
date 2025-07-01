const express = require('express');

const app = express();
const PORT = 7865;

// Handler for the root endpoint GET /
app.get('/', (req, res) => {
  res.status(200).send('Welcome to the payment system');
});

// New endpoint for /cart/:id with regex validation
// The :id parameter must match one or more digits (\d+)
app.get('/cart/:id(\\d+)', (req, res) => {
  const { id } = req.params;
  res.status(200).send(`Payment methods for cart ${id}`);
});

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;
