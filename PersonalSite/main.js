document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.portfolio-card, .resume-card');

    cards.forEach(card => {
        const header = card.querySelector('.card-header');
        const toggle = card.querySelector('.see-more-toggle');
        
        header.addEventListener('click', (event) => {
            if (event.target.closest('a') || event.target.closest('.button-box3')) {
                return; 
            }
            
            if (window.getComputedStyle(toggle).display !== 'none') {
                card.classList.toggle('expanded');
                
                if (card.classList.contains('expanded')) {
                    toggle.textContent = 'See Less ▲';
                } else {
                    toggle.textContent = 'See More ▼';
                }
            }
        });
        
        const updateToggleText = () => {
            if (window.getComputedStyle(toggle).display !== 'none') {
                if (!card.classList.contains('expanded')) {
                    toggle.textContent = 'See More ▼';
                }
            }
        };

        updateToggleText();
        window.addEventListener('resize', updateToggleText);
    });
});