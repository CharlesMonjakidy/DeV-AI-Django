function toggleSidebar(){document.querySelector(".sidebar")?.classList.toggle("open");}
document.querySelectorAll(".side-nav a").forEach(a=>a.addEventListener("click",()=>document.querySelector(".sidebar")?.classList.remove("open")));
