import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Event listener for connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
  // Call the functions after the connection is established
  main();
});

/**
 * Sets a new key-value pair in Redis.
 * @param {string} schoolName - The key to set.
 * @param {string} value - The value to set for the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    // The 'print' function from the redis library is essentially console.log
    // We will log the reply directly to match the desired output format.
    print(`Reply: ${reply}`);
  });
}

/**
 * Displays the value of a given key from Redis.
 * @param {string} schoolName - The key whose value to display.
 */
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(reply);
  });
}

/**
 * Main function to run the required operations in sequence.
 */
function main() {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}
