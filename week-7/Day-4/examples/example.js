// const numbers = [10,11,12,15,20];

// numbers.forEach((i) => {
//   if (i % 2 === 0) {
//     console.log(i);
//   }
// })


// const words = ["wow","hey","bye"];
// let result = words.some((word) => {   
//   if(word[0] === 'w'){
//     console.log(word)
//     return true
//   }
//   return false
// })

// console.log(result);


// const words = ["hello","hey","hola"];

// let results = words.every((word) => { return word[0] === 'h'})
// console.log(results)

// myArr = [10,20,30,40];

// let newArr = myArr.map((val, i, arr) => {
//   return {
//     value: val,
//     index: i
//   };
// });

// console.log(newArr)


let party = [
  {
    desert: 'Chocolate Mousse',
    calories: 30,
  },
  {
    desert: 'Apple Pie',
    calories: 15,
  },
  {
    desert: 'Croissant',
    calories: 50,
  },
  {
    desert: 'Strawberry Icecream',
    calories: 5,
  },
]
let filteredArr = party.filter((item) => {
  return item.desert !== 'Apple Pie'
})
console.log(filteredArr)
let calories = filteredArr.reduce((acc, i) => {
  return acc + i.calories
}, 0)
console.log(calories)