// //Ex1 
// //1. Create these variables and give them values:

// //addressNumber
// //addressStreet
// //country

// let addressNumber = 526
// let addressStreet = "someRoad"
// let country = "Mauritius"

// // 2. Write a variable named globalAddress, and concatenate inside, the variables:

// //     addressNumber
// //     addressStreet
// //     country

// let globalAddress = `I live in ${country}, ${addressNumber} at ${addressStreet}`

// // In order to create a sentence

// // 3. Display globalAddress Example: globalAddress should display « I live in BenYehuda 5, in Israel » 

// console.log(globalAddress)


// // EX2
// let birthYear = 2011
// let futureYear = 2023
// let possibleFutureYear = futureYear - birthYear
// console.log(possibleFutureYear)

//Ex3


// 1. Create a numerically indexed table (ie. an array): pets, like this ['cat','dog','fish','rabbit','cow']

// 2. Display dog

// 3. Add to the array pets, the pet horse. Remove the pet rabbit

// 4. Display the array length

// let array = ['cat','dog','fish','rabbit','cow']



// console.log(array.slice(1,2))
// array.splice(3,1,'horse')
// console.log(array.length)
// console.log(array)


//EX4


// Create a stuctured html file linked to a JS file

// 1. Create an object that has properties "username" and "password". Fill those values in with strings.

// 2. Create an array which contains the object you have made above and name the array "database".

// 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".

// let user = {
//   username: "ashes",
//   password: "aaaaaaaaaaaaaaaaaaashes",
// }
// let database = [user];
// let newsfeed = [
//   {
//     username: "ashes",
//     timeline: 2002,
//   },
//   {
//     username: "ashs",
//     timeline: 22,
//   },
//   {
//     username: "ash",
//     timeline: 202,
//   }
// ]

// console.log(newsfeed)

//EX5


// Make a keyless car!

// This car will only let you drive if you are over 18. Make it do the following:

// Using prompt() and alert(), ask a user for their age.

//     IF they say they are below 18, respond with: "Sorry, you are too young to drive this car. Powering off
//     IF they say they are 18, respond with: "Congratulations on your first year of driving. Enjoy the ride!
//     IF they say they are over 18, respond with: "Powering On. Enjoy the ride!"

// let age = prompt("Please enter your age: ")
// if (age < 18){
//   alert(`Sorry, you are too young to drive this car.`)
// } else if (age == 18){
//   alert(`Congratulations on your first year if driving. Enjoy the ride!`)
// } else if (age > 100){
//   alert(`damn how are you not dead`)
// } else {
//   alert(`Powering On. Enjoy the ride!`)
// }

//EX6


// 1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen.

// Sample Output: //"0 is even" //"1 is odd" //"2 is even"

// for (let i = 0; i < 16; i++) {
//   if (i % 2 ){
//     console.log(`${i} is even`)
//   } else {
//     console.log(`${i} is odd`)
//   }
  
// }

//EX7

// 1. Write a JavaScript for loop that will go through the variable names.

//     if the item is not a string, pass.
//     if the item is a string, check if its first letter is in uppercase. If not, change it to uppercase and then display the name.

// 2. Write a JavaScript for loop that will go through the variable names

//     if the item is not a string, go out of the loop.
//     if the item is a string, display it.
let names= ["john", "sarah", 23, "Rudolf",34]

for (let i = 0; i < names.length;i++){
let item = names[i];
  if (typeof(item) != "string") {
    continue
}
if (item.charAt(0)!= item.charAt(0).toUpperCase()) {
item = names[i].charAt(0).toUpperCase() + item.slice(1)
}
console.log(item)
}
for (let i = 0; i < names.length; i++) {
  let item = names[i];
  if (typeof (item) != 'string') {
    break
  } else {
    console.log(item)
  }
}