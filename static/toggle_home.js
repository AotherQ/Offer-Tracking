function switch_open(){
    var checkbox = document.getElementsByClassName("check")[0];
var bd = document.body;
var slider = document.getElementsByClassName("slider")[0];

var img_box = document.getElementsByClassName("back")[0];

checkbox.toggleAttribute("checked");

if( checkbox.hasAttribute("checked") ){
    document.body.classList.toggle("dark-theme");
    
    
}
else{
    document.body.classList.toggle("dark-theme");
    

    
}
}

