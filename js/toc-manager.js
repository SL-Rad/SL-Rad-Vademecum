    window.addEventListener('DOMContentLoaded', () => {
    
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            const id = entry.target.getAttribute('id');
            if (entry.intersectionRatio > 0) {
                document.querySelector(`nav li a[href="#${id}"]`).parentElement.classList.add('active');
            } else {
                document.querySelector(`nav li a[href="#${id}"]`).parentElement.classList.remove('active');
            }
        });
    });
    
    // Track all sections that have an `id` applied
    document.querySelectorAll('h1[id]').forEach((h1) => {
        observer.observe(h1);
    });

    document.querySelectorAll('h2[id]').forEach((h2) => {
        observer.observe(h2);
    });

    document.querySelectorAll('h3[id]').forEach((h3) => {
        observer.observe(h3);
    });
    
    });
