function switch_open(){
    var checkbox = document.getElementsByClassName("check")[0];
var bd = document.body;
var slider = document.getElementsByClassName("slider")[0];

checkbox.toggleAttribute("checked");

if( checkbox.hasAttribute("checked") ){
    bd.style.backgroundColor = "darkgrey";
    slider.style.backgroundColor = "darkgrey"
    
}
else{
    bd.style.backgroundColor="rgb(83, 83, 83)";
    slider.style.backgroundColor="rgb(83, 83, 83)";

    
}
}

