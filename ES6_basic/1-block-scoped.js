export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    // No variable modification inside the if block
  }

  return [task, task2];
}
