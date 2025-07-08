import kue from 'kue';

// Create a Kue queue.
// Kue will connect to the local Redis server by default.
const queue = kue.createQueue();

// The job data object with a sample phone number and message.
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

// Create a job in the 'push_notification_code' queue.
const job = queue.create('push_notification_code', jobData);

// Event listener for when the job is successfully created and saved to the queue.
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Event listener for when a worker process completes the job.
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for when a worker process fails to complete the job.
job.on('failed', ().log('Notification job failed');
});
