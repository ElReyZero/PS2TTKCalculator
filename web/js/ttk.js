function ttk (shots, distance, velocity, refire_ms, heavyshield) {

    
    var distance  = document.getElementById("distance").value;
    var velocity = document.getElementById("velocity").value;
    var refire_ms = document.getElementById("refire_ms").value;
    var shots = document.getElementById("shots").value;
    var heavyshield = document.getElementById("heavyshield");

    if (heavyshield.checked == true) {
        heavyshield_value = 1450;
    } else {
        heavyshield_value = 1000;
    }

    var ttk_a = ((refire_ms / heavyshield_value) * (shots - 1)) + (distance / velocity);
    document.getElementById("ttk_result").innerHTML = ttk_a;
    
    console.log(ttk_a);

    if (isNaN(ttk_a)) {
        document.getElementById("ttk_result").innerHTML = "∞";
    }
    if (isFinite(ttk_a) == false) {
        document.getElementById("ttk_result").innerHTML = "∞";
    }

    }

// ToDo:
// - Add API calls to grab values for weapons
// - Polish the code and make it more readable
// - Comment the code / add docstrings