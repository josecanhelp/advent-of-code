const { readFile } = require("fs").promises;

let globalArr = [];
let ansArr = [];

function getMaxValueInArray(arr) {
  return arr.reduce((acc, row) => {
    return isNaN(row) ? acc : Math.max(acc, row);
  }, -Infinity);
}

function sumValuesInArray(arr) {
  return arr.reduce((acc, cell) => {
    return parseInt(acc) + parseInt(cell);
  }, 0);
}

function getSumOfTop(num) {
  for (let i = 0; i < num; i++) {
    popMax();
  }
}

function popMax() {
  // What is the maximum value in the global array?
  const maxValue = getMaxValueInArray(globalArr);

  // Add the maximum value to the answer array
  ansArr.push(maxValue);

  // Remove the maximum value from the global array
  globalArr.splice(globalArr.indexOf(maxValue), 1);
}

(async () => {
  // Read the csv input file
  const data = await readFile("./data.csv", {
    encoding: "utf8",
  });

  // Transform the csv input file into a multi-dimensional array.
  // Each empty line begins a new array.
  // Finally, sum the array values in each row
  globalArr = data
    .replace(/\n/g, ",")
    .split(",,")
    .map((row) => {
      return row.split(",").map((cell) => {
        return cell.trim();
      });
    })
    .map(sumValuesInArray);

  // Get the sum of the top 3 values
  getSumOfTop(3);

  console.log(sumValuesInArray(ansArr));
})();
