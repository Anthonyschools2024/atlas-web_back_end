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
  main();
});

/**
 * Main function to perform the hash operations.
 */
function main() {
  const hashKey = 'HolbertonSchools';
  const schoolData = {
    Portland: '50',
    Seattle: '80',
    'New York': '20',
    Bogota: '20',
    Cali: '40',
    Paris: '2',
  };

  // Use hset to store each field-value pair
  for (const [field, value] of Object.entries(schoolData)) {
    client.hset(hashKey, field, value, (err, reply) => {
      // redis.print is essentially console.log for the reply
      print(`Reply: ${reply}`);
    });
  }

  // Use hgetall to retrieve and display the hash
  client.hgetall(hashKey, (err, object) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(object);
  });
}
