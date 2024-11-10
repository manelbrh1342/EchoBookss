
const counters = document.querySelectorAll('.counter');
const speed = 100; // Speed of the count animation

counters.forEach(counter => {
    const updateCount = () => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        
        const increment = target / speed; // Divide the target number to create the animation steps

        if (count < target) {
            counter.innerText = Math.ceil(count + increment);
            setTimeout(updateCount, 20); // Updates every 20 milliseconds
        } else {
            counter.innerText = target;
        }
    };
    
    updateCount();
});
