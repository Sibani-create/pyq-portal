// Function to handle the continuous background movement
function animateBackground() {
    gsap.to('body.dynamic-background-body', {
        backgroundPosition: '10% 10%', // Move slightly
        duration: 15, // Over 15 seconds
        ease: 'power1.inOut',
        repeat: -1, // Repeat indefinitely
        yoyo: true // Go back and forth
    });
}

// --- Initialize Barba.js ---
barba.init({
    transitions: [{
        name: 'dynamic-page-transition',
        
        // This runs on the very first page load
        once(data) {
            const color = getPageColor(data.next.container);
            // Set initial background color and start continuous animation
            gsap.set('body', { backgroundColor: color });
            animateBackground(); // Start the background movement
        },

        // This runs when you click a link to leave a page
        async leave(data) {
            // Animate the current page's content out (fade and slide up)
            await gsap.to(data.current.container, {
                opacity: 0,
                y: -50,
                duration: 0.3
            });
        },

        // This runs when the new page content is ready
        async enter(data) {
            // Get the new page's color
            const newColor = getPageColor(data.next.container);
            
            // --- Animate both at the same time ---

            // 1. Animate the body background color (this will blend with the image)
            gsap.to('body', {
                backgroundColor: newColor,
                duration: 0.4
            });

            // 2. Animate the new page's content in (fade and slide in from below)
            gsap.from(data.next.container, {
                opacity: 0,
                y: 50,
                duration: 0.3
            });
        }
    }]
});

/**
 * Helper function to get the color from the page's data-attribute
 */
function getPageColor(container) {
    const colorEl = container.querySelector('[data-page-color]');
    return colorEl ? colorEl.dataset.pageColor : '#f8f9fa';
}