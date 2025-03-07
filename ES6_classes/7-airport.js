// 7-airport.js
export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Getter for name (optional)
  get name() {
    return this._name;
  }

  // Setter for name (optional)
  set name(newName) {
    this._name = newName;
  }

  // Getter for code
  get code() {
    return this._code;
  }

  // Setter for code (optional)
  set code(newCode) {
    this._code = newCode;
  }

  // Implement toStringTag to customize [object Object]
  get [Symbol.toStringTag]() {
    return this.code;
  }
}
