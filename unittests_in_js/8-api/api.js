const express = require('express');

// Create an instance of the express application
const app = express();
const PORT = 7865;

// Define the handler for the root endpoint GET /
app.get('/', (req, res) => {
  res.status(200).send('Welcome to the payment system');
});

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

// Export the app for potential use in other modules (e.g., more advanced tests)
module.exports = app;
