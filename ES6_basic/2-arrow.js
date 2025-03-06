// 2-arrow.js (Alternative using an arrow function *internally*)
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  this.addNeighborhood = function(newNeighborhood) {
    // Use an arrow function *inside* the method, if needed
    const addToList = (item) => {
      this.sanFranciscoNeighborhoods.push(item); // 'this' refers to the getNeighborhoodsList instance
      return this.sanFranciscoNeighborhoods;
    };
    return addToList(newNeighborhood);
  };
}
