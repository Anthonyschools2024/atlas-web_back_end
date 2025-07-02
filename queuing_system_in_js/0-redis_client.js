import { createClient } from 'redis';

/**
 * Creates a Redis client and connects to the server.
 * Logs messages to the console based on the connection status.
 */
const client = createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
