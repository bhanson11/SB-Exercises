//PART A
function double(arr) {
    return arr.map(function(val) {
      return val * 2;
    });
}

/* Write an ES2015 Version */ 
//ONE-LINER

const double = arr => arr.map(val => val * 2);

//PART B
function squareAndFindEvens(numbers){
    var squares = numbers.map(function(num){
      return num ** 2;
    });
    var evens = squares.filter(function(square){
      return square % 2 === 0;
    });
    return evens;
  }

// replace ALL functions with arrow functions 

const squareAndFindEvens = numbers => numbers.map(val => val ** 2).filter(square => square % 2 === 0)