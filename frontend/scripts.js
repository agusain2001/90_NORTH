window.addEventListener('resize', function() {
    const width = window.innerWidth;
    const container = document.querySelector('.container');

    if (width >= 992 && width <= 1600) {
        container.style.transform = 'scale(0.9)';
    } else if (width >= 700 && width < 767) {
        container.style.transform = 'scale(0.8)';
    } else if (width >= 600 && width < 700) {
        container.style.transform = 'scale(0.75)';
    } else if (width <= 600) {
        container.style.transform = 'scale(0.5)';
    } else {
        container.style.transform = 'scale(1)';
    }
});
