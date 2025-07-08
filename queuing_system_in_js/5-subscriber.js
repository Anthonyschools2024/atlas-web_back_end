import { createClient } from 'redis';

// Create a Redis client
const client = createClient();
const channel = 'holberton school channel';

// Event listener for connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
  // Subscribe to the specified channel
  client.subscribe(channel);
});

// Event listener for messages on the subscribed channel
client.on('message', (subscribedChannel, message) => {
  console.log(message);
  // If the message is KILL_SERVER, unsubscribe and quit
  if (message === 'KILL_SERVER') {
    client.unsubscribe(subscribedChannel);
    client.quit();
  }
});
