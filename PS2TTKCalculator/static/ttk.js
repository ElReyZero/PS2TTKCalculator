function ttk(is_manual = true) {
    if (is_manual) {
        var velocity = document.getElementById("velocity").value;
        var refire_ms = document.getElementById("refire_ms").value;
    }
    else {
        var velocity = parseInt(document.getElementById("velocity").innerHTML.replace(" m/s", ""));
        var refire_ms = parseInt(document.getElementById("refire_ms").innerHTML.replace(" ms", ""));
    }
    var distance = document.getElementById("distance").value;
    var shots = document.getElementById("shots").value;
    var heavyshield = document.getElementById("heavyshield");

    if (heavyshield.checked == true) {
        heavyshield_value = 1450;
    } else {
        heavyshield_value = 1000;
    }
    console.log(velocity)
    var ttk_a = ((refire_ms / heavyshield_value) * (shots - 1)) + (distance / velocity);
    document.getElementById("ttk_result").innerHTML = ttk_a;

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