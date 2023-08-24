const inventory = [
  { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
  { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
  { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
  { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
  { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

let getCarHonda = (carInventory) => carInventory.filter((car) => car.car_make === "Honda");
console.log(getCarHonda(inventory));

let sortCarInventoryByYear = (carInventory) => {
  return carInventory.sort((year1, year2) => year1.car_year - year2.car_year);
}
console.log(sortCarInventoryByYear(inventory));


