document.addEventListener('DOMContentLoaded', function() {
    const activeItem = document.querySelector('.sidebar .active');
    if (activeItem) {
        activeItem.scrollIntoView({ block: 'center' });
    }
})
