// let calculator = (x,opp,y) => {
//   return opp == "+"
//           ? x + y:
//         opp == "-"
//           ? x - y:
//         opp == "*"
//           ? x * y:
//           "invalid";
// }
// console.log(calculator(20,"+",3))
// console.log(calculator(20,"-",3))
// console.log(calculator(20,"*",3))
// console.log(calculator(20,"/",3))

// function verify (name) {            // outer function  
//   function isJohn() {             // inner function
//       return name === "John";     // full access to argument        
//   }
//   if (isJohn()) {
//       console.log("Yep, this is John");
//   } else if (!isJohn()) {
//     console.log("Nope elif, this is not John");
//   } else {
//     console.log("stuff")
//   }
// }
// verify("Johnny");

function winBattle(){
  let experiencePoints = (winBattle)
  ? 10 
  : 1;
  console.log(experiencePoints);

    return true;
}

winBattle();