function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

// questionA();
// Print: it print 'bob' first and then 'Sponge'. 
// Explain: even the timeout set to 0 it will print in the end. the reason - once you set timeout this commend will enter into a queue scheduled to run at the next opportunity.
// and because the code need to be completed before we going into the queue the timeout commend not printed immediately.


// questionB();
// Print: it print 'Promise at B' first and then 'Timeout at B'. 
// Explain: because the promises have a higher priority in the event loop queue compared to timeout.
// meaning - if we have both of them in our code and both of them scheduled at the same time the promises will be execute first nad then the timeout.   



// questionC();
// Print: it print 'Promise at C' first and then 'Timeout at C'.
// Explain: because we define a timeout it will be enter into event queue waiting for the loop event.
// the promise schedules its callback to be executed with a 1000ms delay, and then will be print and after that the code will come back to the timeout.    



// questionD();
// Print: it print 'Sponge' first and then 'Bob', 'Pants' and last but not least 'Square'.
// Explain: hare we have a combine of code synchronous and asynchronous - the first console.log is synchronous and will be print immediately.
// then we come to the timeout line and enter it into the event queue. after that we come to th promise line is asynchronous code.
// after those lines we got to the seconde console.log - synchronous code and will be print immediately. so far we got - Sponge and then Bob.
// and because scheduling of the Promise is faster then  the timeout it will print pants and then square.


// questionE();
// Print:  it print 'Promise at B' first and then 'Promise at C', after those it print 'Timeout at B' and then 'Timeout at C'.
// Explain:  this function contain function B and C. each of this function contains timeout and promise.
// in function B timeout enter to event loop so the promise print first, after that in function c again the timeout enter to the event loop so the promise will be print fist.
// after this it go back and print the timeout in function B and then timeout in function C.