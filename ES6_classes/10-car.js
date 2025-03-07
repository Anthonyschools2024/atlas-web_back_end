// car
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Getter for brand
  get brand() {
    return this._brand;
  }

  // Setter for brand
  set brand(newBrand) {
    this._brand = newBrand;
  }

  // Getter for motor
  get motor() {
    return this._motor;
  }

  // Setter for motor
  set motor(newMotor) {
    this._motor = newMotor;
  }

  // Getter for color
  get color() {
    return this._color;
  }

  // Setter for color
  set color(newColor) {
    this._color = newColor;
  }

  cloneCar() {
    return new Car(this._brand, this._motor, this._color);
  }
}
