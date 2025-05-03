document.getElementById('numberForm').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const nums = [
      Number(document.getElementById('num1').value),
      Number(document.getElementById('num2').value),
      Number(document.getElementById('num3').value),
      Number(document.getElementById('num4').value),
      Number(document.getElementById('num5').value)
    ];
  
    let output = "<h3>Comparison Results:</h3>";
  
    output += `<p>num1 > num2: ${nums[0] > nums[1]}</p>`;
    output += `<p>num2 < num3: ${nums[1] < nums[2]}</p>`;
    output += `<p>num3 >= num4: ${nums[2] >= nums[3]}</p>`;
    output += `<p>num4 <= num5: ${nums[3] <= nums[4]}</p>`;
    output += `<p>num1 == num5: ${nums[0] == nums[4]}</p>`;
    output += `<p>num2 != num3: ${nums[1] != nums[2]}</p>`;
    output += `<p>num3 === num3: ${nums[2] === nums[2]}</p>`;
  
    document.getElementById('result').innerHTML = output;
  });
  