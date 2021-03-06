const showContactForm = document.querySelector('.select-service-btn');
const hideContactForm = document.querySelector('.form-close-btn');


// Stops animation from playing unless refreshed
const tl = new TimelineLite({
    paused: true,
    reversed: true
});

// Cover will animate first...
tl.to('.service-card', 0.5, {
        autoAlpha: 0,
        stagger: 0.2,
    })
    .to('.contact-form-wrap li, .contact-form-wrap', 0.5, {
        delay: 0.2,
        autoAlpha: 1,
        stagger: 0.1,
    })

hideContactForm.addEventListener('click', () => {

    if (tl.isActive()) {
        e.preventDefault();
        e.stopImmediatePropagation();
        return false;
    }
    toggleTween(tl)
})

function toggleTween(tween) {
    tween.reversed() ? tween.play() : tween.reverse();
}

// Button to toggle animation
showContactForm.addEventListener('click', () => {

    if (tl.isActive()) {
        e.preventDefault();
        e.stopImmediatePropagation();
        return false;
    }
    toggleTween(tl)
})

function toggleTween(tween) {
    tween.reversed() ? tween.play() : tween.reverse();
}