function setWeaponToHTML(weapon_data)
{
    document.getElementById("weapon-name").innerHTML = weapon_data.name;
    document.getElementById("weapon-image").src = weapon_data.image_path;
    try
    {
        document.getElementById('manual-calculator').innerHTML = document.getElementById("weapon-calculator").innerHTML;
        document.getElementById('weapon-calculator').remove();
    }
    catch (e){}
    document.getElementById("velocity").innerHTML = weapon_data.muzzle_velocity + " m/s";
    document.getElementById("refire_ms").innerHTML = weapon_data.refire_ms + " ms";
    document.getElementById("distance").value = '';
    document.getElementById("shots").value = '';
    document.getElementById("heavyshield").checked = false;
    document.getElementById('selectedWeaponDiv').style.visibility = "visible";
    
}