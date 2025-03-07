import Building from './5-building.js';

const b = new Building(100); // Should work, direct Building instance
console.log(b);

class TestBuilding extends Building {} // TestBuilding does NOT implement evacuationWarningMessage

try {
    new TestBuilding(200) // Should throw error because TestBuilding lacks evacuationWarningMessage
}
catch(err) {
    console.log(err); // Catch the error and log it
}
