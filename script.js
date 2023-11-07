
alert("Petric get lost! get up and start looking at him")

let goNow = confirm("Go now to search for him, OK?")

if (goNow) {
    alert("Yeeeeyyyyyy! Bob start to searching for Petric!")

    let petricFound = prompt("Did you found Petric?")
    if (petricFound === "yes") {
        alert("congratulations! and keep eye on him next time")

    } else {
        window.location.reload();
    }
    
} else {
    alert("Shame on You!");
    window.location.reload();

}


