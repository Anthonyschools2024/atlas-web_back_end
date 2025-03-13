/**
 * Executes a math function, captures its result or error, and appends a guardrail message.
 *
 * This function accepts a mathFunction (Function) as its argument and creates an array named queue.
 * It executes the provided function inside a try-catch block:
 *   - If the function executes successfully, its return value is appended to the queue.
 *   - If the function throws an error, the error's message (converted to a string) is appended instead.
 * In every case, the message 'Guardrail was processed' is added to the queue.
 *
 * @param {Function} mathFunction - A function expected to perform a mathematical operation.
 * @returns {Array} The queue array with the result/error and the guardrail message.
 */
export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(error.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
