// airport
export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Getter for name (optional, not explicitly asked for but good practice)
  get name() {
    return this._name;
  }

  // Setter for name (optional)
  set name(newName) {
    this._name = newName;
  }

  // Getter for code (optional, but again, good practice)
  get code() {
    return this._code;
  }

  // Setter for code (optional)
  set code(newCode) {
    this._code = newCode;
  }

  // Override toString() method to return the airport code in brackets
  toString() {
    return `[${this._code}]`;
  }
}
