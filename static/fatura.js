fetch('/api/ara')
  .then(response => response.json())
  .then(data => {
    const productBody = document.getElementById('product-body');
    productBody.innerHTML = '';
    data.forEach(row => {
      const tr = document.createElement('tr');

      const idCell = document.createElement('td');
      idCell.textContent = row[0];
      tr.appendChild(idCell);
      
      const firmaCell = document.createElement('td');
      firmaCell.textContent = row[1];
      tr.appendChild(firmaCell);

      const urunCell = document.createElement('td');
      urunCell.textContent = row[2];
      tr.appendChild(urunCell);

      const fiyatCell = document.createElement('td');
      fiyatCell.textContent = row[4];
      tr.appendChild(fiyatCell);

      const urunSayisiCell = document.createElement('td');
      urunSayisiCell.textContent = row[3];
      tr.appendChild(urunSayisiCell);

      const durumCell = document.createElement('td');
      durumCell.textContent = row[5];
      tr.appendChild(durumCell);

      productBody.appendChild(tr);
    });
  })
  .catch(error => {
    console.error('Error retrieving data:', error);
  });



  function switch_open(){
    var checkbox = document.getElementsByClassName("check")[0];
var bd = document.body;
var slider = document.getElementsByClassName("slider")[0];

checkbox.toggleAttribute("checked");

if( checkbox.hasAttribute("checked") ){
    document.body.classList.toggle("dark-theme");
    
}
else{
    document.body.classList.toggle("dark-theme");

    
}
}





