// ✅ Sidebar Active Highlight
const links = document.querySelectorAll(".sidebar a");

links.forEach(link => {
    if(link.href === window.location.href){
        link.style.background = "gold";
        link.style.color = "black";
    }
});


// ✅ Smooth Page Fade Effect
document.body.style.opacity = 0;

window.onload = () => {
    document.body.style.transition = "0.6s";
    document.body.style.opacity = 1;
};


// ✅ Button Hover Animation (Feels Premium)
const buttons = document.querySelectorAll(".big-btn");

buttons.forEach(btn => {

    btn.addEventListener("mouseover", () => {
        btn.style.transform = "scale(1.08)";
    });

    btn.addEventListener("mouseout", () => {
        btn.style.transform = "scale(1)";
    });

});
