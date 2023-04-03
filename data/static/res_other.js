function createStar() {
    const star = document.createElement('div');
    star.classList.add('star');
    star.style.left = `${Math.random() * 100}%`; /* Randomize the position */
    star.style.top = `${Math.random() * 100}%`;
    document.body.appendChild(star); /* Add the star to the body */
    setTimeout(() => star.remove(), 4000); /* Remove the star after 4 seconds */
  }
  
setInterval(createStar, 200); /* Create a new star every 200ms */