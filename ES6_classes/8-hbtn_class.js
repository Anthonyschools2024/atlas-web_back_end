// hbtn_class
export default class HolbertonClass {
  constructor(size, location) {
    this._size = Number(size);
    this._location = String(location);
  }

  // Method to be called when the class is cast into a Number
  valueOf() {
    return this._size;
  }

  // Method to be called when the class is cast into a String
  toString() {
    return this._location;
  }
}
