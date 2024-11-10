
// Toggle dropdown visibility
function toggleDropdown(dropdownId) {
const dropdown = document.getElementById(dropdownId);
const header = dropdown.previousElementSibling; // Get the header to toggle the chevron
if (dropdown.style.display === 'block') {
dropdown.style.display = 'none';
header.classList.remove('active'); // Remove active class when collapsed
} else {
dropdown.style.display = 'block';
header.classList.add('active'); // Add active class when expanded
}
}

// Select option and update the selection text
function selectOption(dropdownId, selectionId, option) {
document.getElementById(selectionId).innerText = option;
document.getElementById(dropdownId).style.display = 'none';

// Remove the active class from the chevron after selection
const header = document.getElementById(dropdownId).previousElementSibling;
header.classList.remove('active');
}
// When the user scrolls down 300px from the top, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
const backToTopBtn = document.getElementById("backToTopBtn");
if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
backToTopBtn.style.display = "block"; // Show button
} else {
backToTopBtn.style.display = "none"; // Hide button
}
}

// Scroll to the top when the button is clicked
function scrollToTop() {
window.scrollTo({
top: 0,
behavior: 'smooth'
});
}


