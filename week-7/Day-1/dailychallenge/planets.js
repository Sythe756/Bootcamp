// Define the planets array with planet objects
let planets = [
  {
    name: "Mercury",
    colorClass: "planet-mercury",
    moons: 0
  },
  {
    name: "Venus",
    colorClass: "planet-venus",
    moons: 0
  },
  {
    name: "Earth",
    colorClass: "planet-earth",
    moons: 1
  },
  {
    name: "Mars",
    colorClass: "planet-earth",
    moons: 2
  },
  {
    name: "Jupiter",
    colorClass: "planet-jupiter",
    moons: 95
  },
  {
    name: "Saturn",
    colorClass: "planet-saturn",
    moons: 146
  },
  {
    name: "Uranus",
    colorClass: "planet-uranus",
    moons: 27
  },
  {
    name: "Neptune",
    colorClass: "planet-neptune",
    moons: 14
  },
  {
    name: "Pluto",
    colorClass: "planet-pluto",
    moons: 5
  },
  {
    name: "Ceres",
    colorClass: "planet-ceres",
    moons: 0
  },
  {
    name: "Eris",
    colorClass: "planet-eris",
    moons: 0
  },
  {
    name: "Haumea",
    colorClass: "planet-haumea",
    moons: 0
  },
  {
    name: "Makemake",
    colorClass: "planet-makemake",
    moons: 0
  },
  {
    name : "Kuiper",
    colorClass: "planet-kuiper",
    moons: 0
  },
  {
    name : "Kepler",
    colorClass: "planet-kepler",
    moons: 0
  },
  {
    name : "Charon",
    colorClass: "planet-charon",
    moons: 0
  },
  {
    name : "Trappist-1",
    colorClass: "planet-trappist-1",
    moons: 0
  },
  {
    name : "Trappist-2",
    colorClass: "planet-trappist-2",
    moons: 0
  },
  {
    name : "Trappist-3",
    colorClass: "planet-trappist-3",
    moons: 0
  }
];

//make planet
function createPlanetElement(planet) {
  let planetDiv = document.createElement("div");
  planetDiv.className = `planet ${planet.colorClass}`;
  planetDiv.textContent = planet.name;

  // Add a unique ID to the planet div
  planetDiv.id = planet.name.toLowerCase();

  // Create moons if the planet has any
  if (planet.moons > 0) {
    for (let i = 0; i < planet.moons; i++) {
      let moonDiv = document.createElement("div");
      moonDiv.className = "moon";
      // Calculate random position within the planet's div
      let moonX = Math.random() * 80 + 10; // Adjust the values as needed
      let moonY = Math.random() * 80 + 10;
      // Apply position as inline style
      moonDiv.style.left = `${moonX}%`;
      moonDiv.style.top = `${moonY}%`;
      planetDiv.appendChild(moonDiv);
    }
  }
  return planetDiv;
}

// Get the section element to append planets
let planetSection = document.querySelector(".listPlanets");

// Loop through the planets array and create planet elements
planets.forEach(planet => {
  let planetElement = createPlanetElement(planet);
  planetSection.appendChild(planetElement);
});
