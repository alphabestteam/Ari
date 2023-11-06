const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2
};

const jellyfishDays = [
    [
        { color: 'pink' },
        { color: 'pink' },
        { color: 'blue' },
        { color: 'green' },
        { color: 'white' },
        { color: 'white' },
    ],
    [
        { color: 'pink' },
        { color: 'pink' },
        { color: 'blue' },
        { color: 'green' },
        { color: 'green' },
        { color: 'green' },
    ],
    [
        { color: 'pink' },
        { color: 'pink' },
        { color: 'pink' },
        { color: 'pink' },
        { color: 'blue' },
        { color: 'green' },
    ]
];

let points = 0;
// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    console.log(`SpongeBob caught a ${jellyfish} jellyfish!`);
    identifyJellyfishAndAddPoints(jellyfish, addPoints);
    console.log(`Score: ${points}`);
}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, addPoints) {
    const species = identifySpecies(jellyfish);
    points += addPoints(species)
    console.log(`Petrick identified a ${species} jellyfish`);
    return addPoints(species);
}

// Score keeping callback function
function addPoints(species) {
    if (species in speciesPoints) {
        return speciesPoints[species];
    }
    return 1;
}

// Helper functions
function identifySpecies(jellyfish) {
    switch (jellyfish) {
        case "pink":
            return "pink spotted";
        case "blue":
            return "blue stinger";
        case "green":
            return "green itches";
        default:
            return "Common!";
    }
}

//The Adventure Starts Here! 
console.log("Let's go jellyfishing!")
for (const day of jellyfishDays) {
    for (const jellyfish of day) {
        catchJellyfish(jellyfish.color, identifyJellyfishAndAddPoints);
    }
}

