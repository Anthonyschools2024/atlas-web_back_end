import kue from 'kue';

// The array of job data
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Create a Kue queue
const queue = kue.createQueue();

// Iterate through the jobs array and create a job for each
jobs.forEach((jobData) => {
  // Create a job in the 'push_notification_code_2' queue
  const job = queue.create('push_notification_code_2', jobData);

  // Event listener for when the job is successfully created
  job.save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  // Event listener for when the job is completed by a worker
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Event listener for when the job fails
  job.on('failed', (errorMessage) => {
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });

  // Event listener for job progress updates
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
