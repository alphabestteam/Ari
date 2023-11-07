const isSufficientFuel = (distance, literPerKm, fuelLeft) => {
      return fuelLeft / literPerKm >= distance;
      // this will return true if we have enough fuel and false if we haven't
}

console.log(isSufficientFuel(10,50,75))