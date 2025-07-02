import { createClient } from 'redis';

/**
 * Creates a Redis client and connects to the server.
 * Logs messages to the console based on the connection status.
 */
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
