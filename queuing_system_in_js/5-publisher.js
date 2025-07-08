import { createClient } from 'redis';

// Create a Redis client
const publisher = createClient();
const channel = 'holberton school channel';

// Event listener for connection errors
publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Event listener for successful connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

/**
 * Publishes a message to a Redis channel after a specified time.
 * @param {string} message - The message to publish.
 * @param {number} time - The delay in milliseconds before publishing.
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish(channel, message);
  }, time);
}

// Call the function with the specified messages and delays
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
