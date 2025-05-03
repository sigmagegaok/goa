document.getElementById('bankForm').addEventListener('submit', function(e) {
    e.preventDefault();
  
    let balance = Number(document.getElementById('balance').value);
    const withdraw = Number(document.getElementById('withdraw').value);
  
    // Using the -= assignment operator
    balance -= withdraw;
  
    document.getElementById('result').innerHTML = `<p>Remaining Balance: ${balance}</p>`;
  });
  