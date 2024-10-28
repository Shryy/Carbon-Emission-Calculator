document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');

    // Ensure the form exists before adding an event listener
    if (form) {
        form.addEventListener('submit', (event) => {
            const distance = parseFloat(form.distance.value);
            const electricity = parseFloat(form.electricity.value);
            const waste = parseFloat(form.waste.value);
            const meals = parseInt(form.meals.value);

            // Check for valid input
            if (isNaN(distance) || isNaN(electricity) || isNaN(waste) || isNaN(meals)) {
                alert('Please fill in all fields correctly.');
                event.preventDefault(); // Prevent form submission
                return; // Exit the function
            }

            if (distance < 0 || electricity < 0 || waste < 0 || meals < 0) {
                alert('Values cannot be negative.');
                event.preventDefault(); // Prevent form submission
                return; // Exit the function
            }
        });
    } else {
        console.error('Form element not found.');
    }
});
