function calculateGrade() {
    const s1 = Number(document.getElementById("score1").value);
    const s2 = Number(document.getElementById("score2").value);
    const s3 = Number(document.getElementById("score3").value);
  
    const average = (s1 + s2 + s3) / 3;
    let grade;
  
    if (average > 90 && average < 100) {
      grade = 'A';
    } else if (average > 70 && average < 80) {
      grade = 'B';
    } else if (average > 50 && average < 65) {
      grade = 'C';
    } else if (average > 25 && average < 50) {
      grade = 'D';
    } else if (average < 25) {
      grade = 'Go study and come back';
    } else {
      grade = 'Grade not determined';
    }
  
    document.getElementById("result").innerText = `Average: ${average.toFixed(2)} → Grade: ${grade}`;
  }
  