let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

let displayGroceries = () => {
    groceries.vegetables.forEach((veggies) => {
      console.log(veggies);
    })
}
displayGroceries();

let cloneGroceries = () => {
  let user = client; 
  user = "Betty";
  console.log(user);
}

let shopping = groceries;
shopping.totalPrice = "35$";
shopping.paid = false;
console.log(shopping);

cloneGroceries();