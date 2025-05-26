document.getElementById('student-form').addEventListener('submit', async (e) => {
  e.preventDefault();

  const student_name = document.getElementById('student_name').value;
  const date = document.getElementById('date').value;
  const city = document.getElementById('city').value;
  const grade = parseFloat(document.getElementById('grade').value);

  let recommendation = '';

  if (grade < 10) {
    recommendation = 'Bad';
  } else if (grade >= 10 && grade <= 16) {
    recommendation = 'Moderate';
  } else if (grade >= 17 && grade < 19) {
    recommendation = 'Very Good';
  } else if (grade >= 19 && grade <= 20) {
    recommendation = 'Excellent';
  } else {
    recommendation = 'Invalid grade';
  }

  document.getElementById('recommendation').innerText = 
    `Student ${student_name} from ${city}, evaluated on ${date}, has a grade of ${grade}/20 → ${recommendation}`;
});
