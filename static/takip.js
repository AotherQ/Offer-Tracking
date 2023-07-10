document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  const productBody = document.getElementById('product-body2');

  form.addEventListener('submit', function(event) {
    const input = document.getElementById('giris');
    const girdi = input.value;

    fetch('/getir', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ giris: girdi })
    })
      .then(response => response.json())
      .then(data => {
        productBody.innerHTML = ''; // Tabloyu temizle

        if (data.length > 0) {
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
        } else {
          const tr = document.createElement('tr');
          const noDataCell = document.createElement('td');
          noDataCell.setAttribute('colspan', '4');
          noDataCell.textContent = 'Veri bulunamadı.';
          tr.appendChild(noDataCell);
          productBody.appendChild(tr);
        }
      })
      .catch(error => {
        console.error('Error retrieving data:', error);
      });

    event.preventDefault(); 
  });
});
