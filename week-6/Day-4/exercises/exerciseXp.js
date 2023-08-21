// //EX1
// const people = ["Greg", "Mary", "Devon", "James"];
// // Part I - Review about arrays

// // Write code to remove “Greg” from the people array.
// people.splice(0, 1);

// // Write code to replace “James” to “Jason”.
// people.splice(2, 1, "Jason");
// // Write code to add your name to the end of the people array.
// people.push("Anas");

// // Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
// console.log(people.indexOf("Mary"));

// // Write code to make a copy of the people array using the slice method.
// //     The copy should NOT include “Mary” or your name.
// //     Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// //     Hint: Check out the documentation for the slice method
// people.slice(1, 3);

// // Write code that gives the index of “Foo”. Why does it return -1 ?
// // It returns -1 because foo isnt in the array


// // Create a variable called last which value is the last element of the array.
// // Hint: What is the relationship between the index of the last element in the array and the length of the array?

// const last = people[people.length - 1];

// console.log(last);
// console.log(people);

// // Part II - Loops

// //     Using a loop, iterate through the people array and console.log each person.
// for (let i = 0; i < people.length; i++) {
//   console.log(people[i]);
// }
// console.log('==============================================================');
// //     Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
// //     Hint: take a look at the break statement in the lesson.
// for (let i = 0; i < people.length; i++) {
//   if (people[i] === "Devon") {
//     break;
//   }
//   console.log(people[i]);
// }

// //EX2

// // 🌟 Exercise 2 : Your favorite colors
// // Instructions

// //     Create an array called colors where the value is a list of your five favorite colors.
// let colors = ["red","blue","white","green","black"]
// //     Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// for (colorChoice in colors){
//   console.log(`My #${colorChoice} choice is ${colors[colorChoice]}`)
// }
// //     Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// //     Hint : create an array of suffixes to do the Bonus



// // 🌟 Exercise 3 : Repeat the question
// // Instructions

// //     Prompt the user for a number.
// //     Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
// user = typeof(prompt("Enter a number: "))
// //     While the number is smaller than 10 continue asking the user for a new number.
// while (user < 10){
//   user = typeof(prompt("Enter a number: "))
// }
// //     Tip : Which while loop is more relevant for this situation?



// 🌟 Exercise 4 : Building Management
// Instructions:

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}


// Review about objects

//     Copy and paste the above object to your Javascript file.

//     Console.log the number of floors in the building.
console.log(building.numberOfFloors);
//     Console.log how many apartments are on the floors 1 and 3.
console.log(building.numberOfAptByFloor.fourthFloor);
//     Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log(building.nameOfTenants[2].numberOfRoomsAndRent[2:1]);
//     Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.


