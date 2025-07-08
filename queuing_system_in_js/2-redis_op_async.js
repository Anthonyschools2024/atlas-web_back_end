import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = createClient();

// Promisify the client.get method
// .bind(client) ensures that 'this' inside the 'get' method refers to the client object
const getAsync = promisify(client.get).bind(client);

// Event listener for connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

/**
 * Sets a new key-value pair in Redis using a callback.
 * @param {string} schoolName - The key to set.
 * @param {string} value - The value to set for the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    // The original redis.print function simply logged the reply.
    // We log it with a prefix to match the example output.
    console.log(`Reply: ${reply}`);
  });
}

/**
 * Asynchronously displays the value of a given key from Redis using async/await.
 * @param {string} schoolName - The key whose value to display.
 */
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}

/**
 * Main async function to run the required operations in sequence.
 */
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

// Call main only after the client has successfully connected.
client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
