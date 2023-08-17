// Instructions

//     Write a JavaScript program that recreates the pattern below.
//     Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
//     Do this Daily Challenge by yourself, without looking at the answers on the internet.

//  *   
//  * *  
//  * * *  
//  * * * * *
//  * * * * * *



let i = "";
for (let j = 0; j < 6; j++) {
  i =  i + "*"
  console.log(i)
}

for (let z = 0; z < 6;z++) {
  let y = ""
  for (let k = 0; k <= z; k++){
    y += "*"
  }
  console.log(y)
}