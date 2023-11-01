const isSufficientFuel = (distance, literPerKm, fuelLeft) => {
const requireFoul = distance * literPerKm
      return requireFoul- fuelLeft > 0
// this will return true if we have enough fuel and false if we haven't
};
  
