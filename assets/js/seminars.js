document.addEventListener('DOMContentLoaded', function() {
  // Get filter buttons
  const upcomingButton = document.querySelector('[data-filter="upcoming"]');
  const pastButton = document.querySelector('[data-filter="past"]');
  
  // Get all seminar cards
  const seminarCards = document.querySelectorAll('.seminar-card');
  const upcomingCards = document.querySelectorAll('.seminar-card.upcoming');
  const pastCards = document.querySelectorAll('.seminar-card.past');
  
  // Add click handlers for filter buttons
  upcomingButton.addEventListener('click', function() {
    upcomingButton.classList.add('is-checked');
    pastButton.classList.remove('is-checked');
    
    // Show upcoming, hide past
    upcomingCards.forEach(card => card.style.display = 'block');
    pastCards.forEach(card => card.style.display = 'none');
  });
  
  pastButton.addEventListener('click', function() {
    pastButton.classList.add('is-checked');
    upcomingButton.classList.remove('is-checked');
    
    // Show past, hide upcoming
    pastCards.forEach(card => card.style.display = 'block');
    upcomingCards.forEach(card => card.style.display = 'none');
  });
  
  // Initialize with upcoming seminars visible
  upcomingCards.forEach(card => card.style.display = 'block');
  pastCards.forEach(card => card.style.display = 'none');
}); 