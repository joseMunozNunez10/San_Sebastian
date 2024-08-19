
// Cuenta los proyectos completados

document.addEventListener('DOMContentLoaded', function() {
    const counterElement = document.getElementById('counter');
    const targetNumber = parseInt(counterElement.textContent);
    let hasRun = false;

    const animateCounter = () => {
        let currentNumber = 0;
        const increment = Math.ceil(targetNumber / 100);

        const interval = setInterval(() => {
            currentNumber += increment;
            if (currentNumber >= targetNumber) {
                currentNumber = targetNumber;
                clearInterval(interval);
            }
            counterElement.textContent = currentNumber;
        }, 10);
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasRun) {
                animateCounter();
                hasRun = true; // Evita que la animación se repita
                observer.unobserve(counterElement); // Deja de observar después de la primera animación
            }
        });
    }, { threshold: 1.0 });

    observer.observe(counterElement);
});


