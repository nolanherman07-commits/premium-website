/* Nestlewood Realty premium site */
const LEAD_EMAIL = "nolan@nestlewoodrealty.com";
// When you set up a free form service (e.g. formspree.io), paste its URL here so
// forms send straight to your inbox. Until then forms open the visitor's email app.
const FORM_ENDPOINT = "";

document.addEventListener("DOMContentLoaded", () => {
  // Hero slideshow
  const slides = document.querySelectorAll(".slide"), dots = document.querySelectorAll(".dots i");
  if (slides.length > 1) {
    let s = 0;
    setInterval(() => {
      slides[s].classList.remove("on"); dots[s] && dots[s].classList.remove("on");
      s = (s + 1) % slides.length;
      slides[s].classList.add("on"); dots[s] && dots[s].classList.add("on");
    }, 6000);
  }

  // Review slider
  document.querySelectorAll(".slider").forEach((sl) => {
    const items = sl.querySelectorAll(".rv"), count = sl.querySelector(".rv-count");
    let i = 0;
    const show = (n) => { items[i].classList.remove("on"); i = (n + items.length) % items.length; items[i].classList.add("on"); count.textContent = `${i + 1} / ${items.length}`; };
    sl.querySelector(".rv-prev").onclick = () => show(i - 1);
    sl.querySelector(".rv-next").onclick = () => show(i + 1);
    setInterval(() => show(i + 1), 9000);
  });

  // Mobile menu
  const mb = document.querySelector(".menu-btn"), nav = document.querySelector(".nav");
  if (mb) mb.onclick = () => {
    const open = nav.style.display === "flex";
    Object.assign(nav.style, open ? { display: "" } : { display: "flex", position: "absolute", top: "84px", left: 0, right: 0, flexDirection: "column", background: "#fff", padding: "1.4rem", gap: "1.2rem", boxShadow: "0 12px 24px rgba(0,0,0,.1)" });
  };

  // Mortgage calculator
  const $ = (id) => document.getElementById(id);
  if ($("c-price")) {
    const money = (n) => "$" + Math.round(n).toLocaleString("en-US");
    const calc = () => {
      const price = +$("c-price").value || 0, down = (+$("c-down").value || 0) / 100;
      const r = (+$("c-rate").value || 0) / 100 / 12, n = (+$("c-term").value || 30) * 12, extra = +$("c-extra").value || 0;
      const loan = price * (1 - down);
      const pi = r ? loan * r / (1 - Math.pow(1 + r, -n)) : loan / n;
      $("c-pay").textContent = money(pi + extra); $("c-pi").textContent = money(pi); $("c-ti").textContent = money(extra); $("c-loan").textContent = money(loan);
    };
    document.querySelectorAll(".calc input").forEach((el) => el.addEventListener("input", calc)); calc();
  }

  // Lead forms
  document.querySelectorAll(".lead-form").forEach((f) => f.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = new FormData(f), btn = f.querySelector("button"), label = btn.textContent;
    // Free guide: show a download button once they sign up
    const showGuide = () => {
      if (!f.dataset.guide || f.nextElementSibling?.classList.contains("guide-dl")) return;
      f.insertAdjacentHTML("afterend", `<a class="btn btn-dark guide-dl" style="margin-top:1rem" href="${f.dataset.guide}" download>Download Your Free Guide (PDF)</a>`);
    };
    if (FORM_ENDPOINT) {
      btn.textContent = "Sending...";
      data.append("_subject", f.dataset.subject || "Website lead");
      try { const r = await fetch(FORM_ENDPOINT, { method: "POST", body: data, headers: { Accept: "application/json" } }); if (!r.ok) throw 0;
        f.reset(); btn.textContent = "Sent! I'll be in touch soon."; showGuide(); } catch { btn.textContent = label; alert("Something went wrong. Please call or text " + LEAD_EMAIL); }
      return;
    }
    showGuide();
    const body = [...data].map(([k, v]) => `${k}: ${v}`).join("\n");
    location.href = `mailto:${LEAD_EMAIL}?subject=${encodeURIComponent(f.dataset.subject || "Website lead")}&body=${encodeURIComponent(body)}`;
  }));

  // Reveal on scroll
  const io = new IntersectionObserver((es) => es.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } }), { threshold: 0.12 });
  document.querySelectorAll(".rev").forEach((el) => io.observe(el));
});
