const form = document.getElementById('survey-form');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const recommendationInput = document.getElementById('recommendation');
const navigationInput = document.getElementById('navigation');
const accuracyInput = document.getElementById('accuracy');
const feedbackYesInput = document.getElementById('feedback-yes');
const feedbackNoInput = document.getElementById('feedback-no');
const commentsInput = document.getElementById('comments');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(form);

  const surveyResults = {
    name: formData.get('name'),
    email: formData.get('email'),
    recommendation: formData.get('recommendation'),
    navigation: formData.get('navigation'),
    accuracy: formData.get('accuracy'),
    feedback: formData.get('feedback'),
    comments: formData.get('comments')
  };

  console.log(surveyResults);

  // Here you can add your code to send the survey results to your server
});
