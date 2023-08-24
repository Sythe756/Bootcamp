const gameInfo = [
  {
    username: "john",
    team: "red",
    score: 5,
    items: ["ball", "book", "pen"]
  },
  {
    username: "becky",
    team: "blue",
    score: 10,
    items: ["tape", "backpack", "pen"]
  },
  {
    username: "susy",
    team: "red",
    score: 55,
    items: ["ball", "eraser", "pen"]
  },
  {
    username: "tyson",
    team: "green",
    score: 1,
    items: ["book", "pen"]
  },
];

let userNames = [];
gameInfo.forEach((user) => {
  userNames.push(user.username + "!");
});
console.log(userNames);

let winners = [];
gameInfo.forEach((winner) => {
  if (winner.score > 5) {
    winners.push(winner.username+" is "+" the "+" winner of the game!");
  }
});
console.log(winners);
// 3. Find and display the total score of the users. (Hint: The total score is 71)
let total = 0;
gameInfo.forEach((user) => {
  return total += user.score;
});
console.log(total);