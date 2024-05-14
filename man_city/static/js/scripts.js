document.addEventListener("DOMContentLoaded", function() {
    var scrollToTopButton = document.querySelector(".scroll-to-top");

    scrollToTopButton.addEventListener("click", function() {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
})