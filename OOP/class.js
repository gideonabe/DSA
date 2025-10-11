// Define a Class

class Car {
  constructor(brand, color){
    this.brand = brand; // property
    this.color = color; // property
    this.speed = 0; // default value
  }

  drive(){
    this.speed += 10;
    console.log(`${this.brand} is driving at ${this.speed} km/h`)
  }

  brake() {
    this.speed -= 10;
    console.log(`${this.brand} slowed down to ${this.speed} km/h`);
  }
}

// Create Objects (Instances)
const myCar = new Car("Toyota", "Red");
const yourCar = new Car("BMW", "Black");

myCar.drive();     // Toyota is driving at 10 km/h
yourCar.drive();   // BMW is driving at 10 km/h
myCar.brake();     // Toyota slowed down to 0 km/h


// Inheritance (Reusing Classes)
class ElectricCar extends Car {
  constructor(brand, color, battery) {
    super(brand, color);       // Call parent constructor
    this.battery = battery;    // New property
  }

  charge() {
    console.log(`${this.brand} is charging. Battery: ${this.battery}%`);
  }
}

const tesla = new ElectricCar("Tesla", "White", 100);
tesla.drive();     // Tesla is driving at 10 km/h
tesla.charge();    // Tesla is charging. Battery: 100%



// Encapsulation -  restricting direct access to some of the object’s internal components, usually by using private properties and controlled access via getters and setters.
class Car {
  #speed = 0; // private field using #

  constructor(brand, color) {
    this.brand = brand;
    this.color = color;
  }

  drive() {
    this.#speed += 10;
    console.log(`${this.brand} is driving at ${this.#speed} km/h`);
  }

  brake() {
    this.#speed = Math.max(0, this.#speed - 10);
    console.log(`${this.brand} slowed down to ${this.#speed} km/h`);
  }

  // Getter for speed
  getSpeed() {
    return this.#speed;
  }
}



// Polymorphism - allows different classes to define different implementations of the same method.
class ElectricCar extends Car {
  constructor(brand, color, battery) {
    super(brand, color);
    this.battery = battery;
  }

  drive() {
    if (this.battery <= 0) {
      console.log(`${this.brand} can't drive. Battery is empty.`);
    } else {
      this.battery -= 5;
      // Call the parent method to increase speed
      super.drive();
      console.log(`Battery remaining: ${this.battery}%`);
    }
  }

  charge() {
    console.log(`${this.brand} is charging. Battery: ${this.battery}%`);
  }
}
